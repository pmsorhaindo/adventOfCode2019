f = open('input.txt')
line = f.readline()

ADD_OP_CODE = 1
MULT_OP_CODE = 2
INPUT_OP_CODE = 3
OUTPUT_OP_CODE = 4

def load_program():
  return [int(s) for s in line.split(',')]


def ammend_program(noun, verb, program_list):
  program_list[1] = noun
  program_list[2] = verb
  return program_list

def run_add_operation(program_list, instruction_pointer, parsed_instruction):
  a = program_list[program_list[instruction_pointer+1]] if int(parsed_instruction[2]) == 0 else program_list[instruction_pointer+1]
  b = program_list[program_list[instruction_pointer+2]] if int(parsed_instruction[1]) == 0 else program_list[instruction_pointer+2]
  program_list[program_list[instruction_pointer+3]] = a + b
  print(a,b, a+b)
  return (program_list, 4)

def run_mult_operation(program_list, instruction_pointer, parsed_instruction):
  a = program_list[program_list[instruction_pointer+1]] if int(parsed_instruction[2]) == 0 else program_list[instruction_pointer+1]
  b = program_list[program_list[instruction_pointer+2]] if int(parsed_instruction[1]) == 0 else program_list[instruction_pointer+2]
  program_list[program_list[instruction_pointer+3]] = a * b
  print(a,b, a*b)
  return (program_list, 4)

def run_input_operation(program_list, instruction_pointer, parsed_instruction):
  program_list[program_list[instruction_pointer+1]] = 1
  return (program_list, 2)

def run_output_operation(program_list, instruction_pointer, parsed_instruction):
  print(program_list[instruction_pointer+1])
  return (program_list, 2)

def run_operation_at_pointer(program_list, instruction_pointer):
  parsed_instruction = list(str(program_list[instruction_pointer]))
  while len(parsed_instruction) != 5:
    parsed_instruction.insert(0,0)
  print(parsed_instruction, program_list[instruction_pointer+1], program_list[instruction_pointer+2])
  if(program_list[instruction_pointer] % 100 is ADD_OP_CODE):
    return run_add_operation(program_list, instruction_pointer, parsed_instruction)
  if(program_list[instruction_pointer] % 100 is MULT_OP_CODE):
    return run_mult_operation(program_list, instruction_pointer, parsed_instruction)
  if(program_list[instruction_pointer] % 100 is INPUT_OP_CODE):
    return run_input_operation(program_list, instruction_pointer, parsed_instruction)
  if(program_list[instruction_pointer] % 100 is OUTPUT_OP_CODE):
    return run_output_operation(program_list, instruction_pointer, parsed_instruction)

def process_program(program_list, instruction_pointer):
  program_list, param_jump = run_operation_at_pointer(program_list, instruction_pointer)
  instruction_pointer = instruction_pointer + param_jump
  if (program_list[instruction_pointer] is 99):
    return program_list[0]
  else:
    return process_program(program_list, instruction_pointer)



print(process_program(load_program(), 0))