from pyspark.sql import SparkSession
import re

# 1. Créer la session Spark
spark = SparkSession.builder \
    .appName("WordCount") \
    .getOrCreate()

# 2. Lire le fichier depuis HDFS
hdfs_input_path = "hdfs://localhost:9000/user/khadija/bigdata/input/books_clean.txt"
lines = spark.read.text(hdfs_input_path).rdd.map(lambda r: r[0])

# 3. Mapper : nettoyer et découper en mots
words = lines.flatMap(lambda line: re.findall(r'\b\w+\b', line.lower()))

# 4. Compter les occurrences
word_counts = words.map(lambda word: (word, 1)).reduceByKey(lambda a, b: a + b)

# 5. Sauvegarder le résultat dans HDFS
hdfs_output_path = "hdfs://localhost:9000/user/khadija/bigdata/output_spark"
# Supprimer le dossier de sortie s'il existe déjà
import subprocess
subprocess.run(["hdfs", "dfs", "-rm", "-r", hdfs_output_path], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

word_counts.saveAsTextFile(hdfs_output_path)

# 6. Arrêter Spark
spark.stop()

print(f" WordCount terminé. Résultat sauvegardé dans {hdfs_output_path}")

