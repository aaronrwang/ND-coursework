#!/bin/bash

extract_archive() {
    local archive=$1
    local destination=$2
    case "${archive}" in
        *.tar.gz|*.tar) tar -xf "$archive" -C "$destination" > /dev/null 2>&1 ;;
        *.zip) unzip "$archive" -d "$destination" > /dev/null 2>&1 ;;
        *) echo "Unsupported archive format: $archive"; return 1 ;;
    esac
    return $?
}

check_malicious_urls() {
    local file=$1
    while IFS=, read -r url; do
        if grep -q "$url" "$file"; then
            echo "Malicious URL found: $url"
            return 1
        fi
    done < "$MALICIOUS_URLS_CSV"
    return 0
}

# Function to check for sensitive content
check_sensitive_content() {
    local file=$1
    while read -r keyword; do
        if grep -qi "$keyword" "$file"; then
            echo "Sensitive content found: $keyword"
            return 1
        fi
    done < "$SENSITIVE_CONTENT_KEYWORDS"
    return 0
}

log_message() {
    echo "$(date +"%Y-%m-%d %H:%M:%S") - $1" >> "$LOG_FILE"
}

function cleanup {
    echo ""
    echo "Ctrl+C pressed. Cleaning up..."
    rm -r "$temp_dir" 2>/dev/null
    log_message "Script exited."
    exit 1 
}

trap cleanup SIGINT

if [ $# -ne 5 ]; then
    echo "Usage: $0 <toscan_dir> <approved_dir> <quarantined_dir> <log_dir> <url_file>" 
    exit 1
fi

if ! [ -d "$1" ]; then
    echo "$1 is not a directory."
    exit 1
fi

if ! [ -d "$2" ] && [ "$2" != "/dev/null"]; then
    echo "$2 is not a directory."
    exit 1
fi

if ! [ -d "$3" ] && [ "$3" != "/dev/null"]; then
    echo "$3 is not a directory."
    exit 1
fi

if ! [ -d "$4" ] && [ "$4" != "/dev/null"]; then
    echo "$4 is not a directory."
    exit 1
fi

if ! [ -f "$5" ]; then
    echo "$5 is not a file."
    exit 1
fi

WATCH_DIR=$1            # Directory to watch for new archives
APPROVED_DIR=$2     # Directory to store approved archives
QUARANTINE_DIR=$3  # Directory to store quarantined archives
LOG_DIR=$4          # Directory that holds logs of script processes
MALICIOUS_URLS_CSV=$5  # CSV with malicious URLs
temp_dir="./temp"

# Note when the script is started
BASENAME_LOG_FILE=$(date +"%Y-%m-%d")
LOG_FILE="$LOG_DIR/$BASENAME_LOG_FILE.log"
log_message "Script started."

while true; do
    for archive in "$1"*; do
        if [ -f "$archive" ]; then
            filename=$(basename "$archive")
            mkdir -p "$temp_dir"
            if ! extract_archive "$archive" "$temp_dir"; then
                # If extraction fails, quarantine the archive
                echo "Extraction failed for $archive. Quarantining..."
                mv "$archive" "$QUARANTINE_DIR/"
                echo -e "$filename\nCANNOTEXTRACT" > "$QUARANTINE_DIR/$filename.reason"
                continue
            fi

            FLAGGED=0
            for FILE in $(find "$temp_dir" -type f); do
                BASEFILE=$(basename "$FILE")
                if [[ "$(basename "$FILE")" == ._* ]]; then
                    echo "Ignoring $FILE"
                    continue  # Skip this file and move to the next
                fi

                if output=$(sh sbs.sh "$MALICIOUS_URLS_CSV" "$FILE" 2>/dev/null | grep "MALICIOUSURL"); then
                    URL=$(echo $output | sed 's/.*MALICIOUSURL: "\([^"]*\)".*/\1/')
                    echo "MALICIOUSURL detected in $FILE"
                    echo -e "$FILE\nMALICIOUSURL\n$url" > "$QUARANTINE_DIR/$BASEFILE.reason"
                    log_message "$archive, QUARANTINE, MALICIOUSURL, $URL."
                    mv $archive "$QUARANTINE_DIR"
                    FLAGGED=1
                    break
                fi

                if output=$(sh sf.sh $FILE 2> /dev/null | grep "SENSITIVE"); then
                    SENSITIVE=$(echo $output | sed 's/SENSITIVE: //')
                    echo "SENSITIVE detected in $FILE"
                    echo -e "$BASEFILE\nSENSITIVE\n$SENSITIVE" > "$QUARANTINE_DIR/$BASEFILE.reason"
                    log_message "$archive, QUARANTINE, SENSITIVE, $SENSITIVE."
                    mv $archive "$QUARANTINE_DIR"
                    FLAGGED=1
                    break
                fi

                echo "File $FILE passed all checks. Moving to approved directory..."
                
            done

            if [ $FLAGGED -eq 0 ]; then
                log_message "$archive, APPROVE."
                mv "$archive" "$APPROVED_DIR/"
            fi

            rm -r "$temp_dir" 2>/dev/null
        fi
    done
    sleep 1
done
