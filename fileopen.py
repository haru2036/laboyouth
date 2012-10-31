
		with open("strarf_serif.txt","rb") as f:
			for line in f:
				srctxt.append(line)
		modelGen=trigramModelGenerator.trigramModelGenerator(srctxt)
		freq1=modelGen.generateModel()
