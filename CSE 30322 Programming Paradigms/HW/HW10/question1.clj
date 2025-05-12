(defn square [n]
  (let [squares (map #(* % %) (range 1 (inc n)))]
    (doseq [sq squares]
      (println sq))
    (reduce + squares)))

(def n (Integer/parseInt (first *command-line-args*)))
(def result (square n))
(printf "Sum = %d\n" result)
