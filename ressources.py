def charger_image(chemin, largeur=60):
    import numpy
    import PIL.Image
    img = numpy.mean(numpy.array(PIL.Image.open(chemin)), axis=2)
    scale = int(img.shape[1] / largeur)
    scaled = [
        [
            numpy.mean(img[i:i + scale * 2, j:j + scale].ravel())
            for j in range(0, img.shape[1], scale)
        ]
        for i in range(0, img.shape[0], scale * 2)
    ]
    return scaled, len(scaled), len(scaled[0])