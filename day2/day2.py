f = open('input.txt')
line = f.readline()

ADD_OP_CODE = 1
MULT_OP_CODE = 2

def load_program():
  return [int(s) for s in line.split(',')]


def ammend_program(noun, verb, program_list):
  program_list[1] = noun
  program_list[2] = verb
  return program_list

def run_add_operation(program_list, instruction_pointer):
  a = program_list[program_list[instruction_pointer+1]]
  b = program_list[program_list[instruction_pointer+2]]
  program_list[program_list[instruction_pointer+3]] = a + b
  return program_list

def run_mult_operation(program_list, instruction_pointer):
  a = program_list[program_list[instruction_pointer+1]]
  b = program_list[program_list[instruction_pointer+2]]
  program_list[program_list[instruction_pointer+3]] = a * b
  return program_list

def  run_operation_at_pointer(program_list, instruction_pointer):
  if(program_list[instruction_pointer] is ADD_OP_CODE):
    return run_add_operation(program_list, instruction_pointer)
  if(program_list[instruction_pointer] is MULT_OP_CODE):
    return run_mult_operation(program_list, instruction_pointer)

def process_program(program_list, instruction_pointer):
  program_list = run_operation_at_pointer(program_list, instruction_pointer)
  instruction_pointer = instruction_pointer + 4
  if (program_list[instruction_pointer] is 99):
    return program_list[0]
  else:
    return process_program(program_list, instruction_pointer)

def find_noun_verb():
  noun = 0
  verb = 0
  output = 0
  original_program_list = load_program()
  while output != 19690720:
    program_list = load_program()
    ammend_program(noun, verb, program_list)
    try:
      output = process_program(program_list, 0) # 0 puts instruction pointer at start
    except:
      output = 0
    if output == 19690720:
      return (noun,verb)
    if verb < 100:
      verb = verb + 1
    elif verb is 100:
      verb = 0
      noun = noun + 1 
    elif noun is 100:
      return (-1, -1)
  return (noun, verb)

noun, verb = (find_noun_verb())

print(100 * noun + verb)