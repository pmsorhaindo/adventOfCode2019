import itertools
from int_computer import IntComputer

phases = itertools.permutations(range(5,10))
largest_output = 0
largest_output_sequence = None

for phase_seq in phases:
  phase_sequence = list(phase_seq)
  output_signal = 0
  ics = []
  ic_pointer = 0
  complete = False 

  for phase in phase_sequence:
    ics.append(IntComputer(phase))
  

  while ics[4].complete == False:
    ics[ic_pointer % 5].input(output_signal)
    output_signal = ics[ic_pointer % 5].run()
    if output_signal == None:
      output_signal = 0
    ic_pointer = ic_pointer + 1

  if (output_signal > largest_output):
    largest_output = output_signal
    largest_output_sequence = phase_sequence

print(largest_output, largest_output_sequence)