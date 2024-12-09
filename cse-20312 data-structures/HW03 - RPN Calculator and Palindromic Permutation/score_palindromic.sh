#!/bin/bash

# Configuration

PROGRAM=palindromic
EXECUTABLE=./$PROGRAM
WORKSPACE=/tmp/$PROGRAM.$(id -u)
POINTS=25
FAILURES=0

# Functions

error() {
    echo "$@"
    [ -r $WORKSPACE/test ] && cat $WORKSPACE/test
    echo
    FAILURES=$((FAILURES + 1))
}

cleanup() {
    STATUS=${1:-$FAILURES}
    rm -fr $WORKSPACE
    exit $STATUS
}

# Test Cases

input1() {
    cat <<EOF
a
aa
aaa
aab
baa
abcabc
abcabcd
abcabcdd
abcdefgfedcba
abcdefggfedcba
EOF
}

output1() {
    cat <<EOF
YEAH
YEAH
YEAH
YEAH
YEAH
YEAH
YEAH
YEAH
YEAH
YEAH
EOF
}

input2() {
    cat <<EOF
ab
ba
abc
abcdeabc
abcdecba
EOF
}

output2() {
    cat <<EOF
NOPE
NOPE
NOPE
NOPE
NOPE
EOF
}

# Setup

mkdir $WORKSPACE

trap "cleanup" EXIT
trap "cleanup 1" INT TERM

# Tests

echo "Testing $PROGRAM ..."

printf " %-40s ... " "$PROGRAM input1 (output)"
diff -y -b <(input1 | ./$EXECUTABLE) <(output1) &> $WORKSPACE/test
if [ $? -ne 0 ]; then
    error "Failure"
else
    echo "Success"
fi

printf " %-40s ... " "$PROGRAM input2 (output)"
diff -y -b <(input2 | ./$EXECUTABLE) <(output2) &> $WORKSPACE/test
if [ $? -ne 0 ]; then
    error "Failure"
else
    echo "Success"
fi

printf " %-40s ... " "$PROGRAM input1 (valgrind)"
input1 | valgrind --leak-check=full ./$EXECUTABLE &> $WORKSPACE/test
if [ $? -ne 0 ] || [ $(awk '/ERROR SUMMARY:/ {print $4}' $WORKSPACE/test) -ne 0 ]; then
    error "Failure"
else
    echo "Success"
fi

printf " %-40s ... " "$PROGRAM input2 (valgrind)"
input2 | valgrind --leak-check=full ./$EXECUTABLE &> $WORKSPACE/test
if [ $? -ne 0 ] || [ $(awk '/ERROR SUMMARY:/ {print $4}' $WORKSPACE/test) -ne 0 ]; then
    error "Failure"
else
    echo "Success"
fi

# This is searching for the number of occurences of "Success" in this script itself
TESTS=$(($(grep -c Success $0) - 2))

echo
echo "   Score $(echo "scale=4; ($TESTS - $FAILURES) / $TESTS.0 * $POINTS.0" | bc | awk '{ printf "%0.2f\n", $1 }' ) / $POINTS.00"
printf "  Status "
if [ $FAILURES -eq 0 ]; then
    echo "Success"
else
    echo "Failure"
fi
echo