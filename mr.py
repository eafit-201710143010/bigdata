from mrjob.job import MRJob

class MRWordFrequencyCount(MRJob):

    def mapper(self, _, line):
        try:
            yield 'Salario promedio empleado: ' + line.split(',')[0], int(line.split(',')[2])
            yield 'Salario promedio secEcon: ' + line.split(',')[1], int(line.split(',')[2])
            yield 'SecEcon por empleado: ' + line.split(',')[0], line.split(',')[1]
        except:
            pass

    def reducer(self, key, values):
        if str(key).startswith('Salario'):
            lista = []
            for item in values:
                lista.append(item)
            yield key, int(sum(lista)/len(lista))
        else:
            lista = []
            for item in values:
                if not item in lista:
                    lista.append(item)
            yield key, int(len(lista))

if __name__ == '__main__':
    MRWordFrequencyCount.run()