import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-f',"--fahrenheit",default=100,help='fahrenheit')
#parser.add_argument('-C',"--celcius",default=0.6,help='celcus')
args=parser.parse_args()

F=args.fahrenheit
c = args.celcius

print F
