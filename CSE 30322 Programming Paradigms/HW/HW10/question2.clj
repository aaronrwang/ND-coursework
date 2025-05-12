(ns taxation)

(defn tax [amount rate]
  (let [result (* amount (/ (double rate) 100.0))]
    (/ (Math/floor (* result 100)) 100.0)))

(ns application)

(println (taxation/tax 117 7))