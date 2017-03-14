import HTSeq
import argparse


parser = argparse.ArgumentParser() #simplifys the wording of using argparse as stated in the python tutorial
parser.add_argument("-i", type=str, action='store',  dest='input', help="input the read file") # allows input of the forward read
parser.add_argument('-fasta', action='store_true', default=False, dest='fasta_switch', help='Input is fasta')
parser.add_argument('-fastq', action='store_true', default=False, dest='fastq_switch', help='Input is fastq')
args = parser.parse_args()

INPUT = str(args.input)



if args.fasta_switch == True:
    inputfile = HTSeq.FastaReader( INPUT )
if args.fastq_switch == True:
	inputfile = HTSeq.FastqReader( INPUT, "phred")


output1 = open('Split_1.fa','w')
output2 = open('Split_2.fa','w')
output3 = open('Split_3.fa','w')
output4 = open('Split_4.fa','w')
output5 = open('Split_5.fa','w')
output6 = open('Split_6.fa','w')
output7 = open('Split_7.fa','w')
output8 = open('Split_8.fa','w')
output9 = open('Split_9.fa','w')
output10 = open('Split_10.fa','w')


count = 0
for read in inputfile:
	count +=1
	if count%10 == 0:
		output1.write('>' + read.name + '\n')
		output1.write(read.seq + '\n')
	elif count%10 == 1:
		output2.write('>' + read.name + '\n')
		output2.write(read.seq + '\n')
	elif count%10 == 2:
		output3.write('>' + read.name + '\n')
		output3.write(read.seq + '\n')
	elif count%10 == 3:
		output4.write('>' + read.name + '\n')
		output4.write(read.seq + '\n')
	elif count%10 == 4:
		output5.write('>' + read.name + '\n')
		output5.write(read.seq + '\n')
	elif count%10 == 5:
		output6.write('>' + read.name + '\n')
		output6.write(read.seq + '\n')
	elif count%10 == 6:
		output7.write('>' + read.name + '\n')
		output7.write(read.seq + '\n')
	elif count%10 == 7:
		output8.write('>' + read.name + '\n')
		output8.write(read.seq + '\n')
	elif count%10 == 8:
		output9.write('>' + read.name + '\n')
		output9.write(read.seq + '\n')
	elif count%10 == 9:
		output10.write('>' + read.name + '\n')
		output10.write(read.seq + '\n')


output1.close()
output2.close()
output3.close()
output4.close()
output5.close()
output6.close()
output7.close()
output8.close()
output9.close()
output10.close()









