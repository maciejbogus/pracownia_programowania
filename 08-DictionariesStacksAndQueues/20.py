import urllib.request, json 
with urllib.request.urlopen("http://api.nbp.pl/api/exchangerates/rates/c/eur/last/150/?format=json") as url:
    c = open("exch.txt", "w").close()
    with open("exch.txt", "a") as file:
        data = json.loads(url.read())
        for key, exchange in data.items():
            if(key=="rates"):
                file.write("{:<15}{:<15}{:<15}\n".format("Date", "Buying Rate", "Selling Rate"))
                file.write("{:<15}{:<15}{:<15}\n".format("===============", "===============", "==============="))
                for element in exchange:
                    file.write("{:<15}{:<15}{:<15}\n".format(element['effectiveDate'], element['bid'], element['ask']))