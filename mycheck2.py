def write_output(results, output_file_name):
    output_file = open(output_file_name, "w")
    for word, count in results:
        output_file.write("\n".join(["%s,%s" % (word, count)]) + "\n")
    output_file.close()


results = [("bob", 1), ("cat", 4), ("juice", 1)]
output_file_name = "output1111.txt"

write_output(results, output_file_name)
