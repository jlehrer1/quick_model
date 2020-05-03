# Quick Model
A silly project I'm throwing together. Run from the command line and recieve a saved Tensorflow CNN trained to detect images of the object of your choice! Classification might not be good, but hey, it's made just for you!

Usage:
```
model.py <params file> <search term> <write location>
```

Where `params file` is a file containing your Google Custom Search API Key and CX as so:
```
<KEY>
<CX>
```

Outputs a saved `.tf` model into `models/`

TODO: Add data augmentation to increase score
