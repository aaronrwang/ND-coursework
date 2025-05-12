; hardcodes the file path to the CSV
(def filepath "./temperatures.txt")

; parse into rows using slup and str/split by new lines #"\n"
(def rows (clojure.string/split (slurp filepath) #"\n"))


; use `map` to make it a collection of floating point numbers
(def rows (map (fn [x] (Double/parseDouble x)) rows))

(defn avg [p] (double (/ (reduce + p)  (count p))))

(defn ftoc [t] (/ (double (* (- t 32) 5)) 9.0))
(println "min = " (ftoc (apply min rows)))
(println "max = " (ftoc (apply max rows)))
(println "average = " (ftoc (avg rows)))