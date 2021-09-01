from flask import Flask, render_template
from requests import request

app = Flask(__name__)

@app.route('/', methods=['GET'])
def main():         
    f = open('C:\\Users\\ME\\Desktop\\test\\python\\Flask\\read_txt_word\\word.txt','r')
    s = f.read()
    f.close()

    if s == '1':
        return render_template('first.html')
    elif s == '2':
        return render_template('second.html')
    elif s == '3':
        return render_template('third.html')
    else:
        return print("Bye")

@app.route('/first')
def first():
	return render_template('first.html')

@app.route('/second')
def second():
	return render_template('second.html')

@app.route('/third')
def third():
	return render_template('third.html')    
        
                   
if __name__ == '__main__':
	app.run(host='192.168.10.104',port='5000',debug=True)