# Quick Model
Run from the command line and recieve a saved Tensorflow CNN trained to detect images of the object of your choice!

To make sure you have all required libraries, run 
```
pip install -r requirements.txt
```

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
