f = open('input.txt')
line = f.readline()

program_pointer = 0
ADD_OP_CODE = 1
MULT_OP_CODE = 2

program_list = [int(s) for s in line.split(',')]

def ammend_program():
  program_list[1] = 12
  program_list[2] = 2

def run_add_operation(program_list, program_pointer):
  a = program_list[program_list[program_pointer+1]]
  b = program_list[program_list[program_pointer+2]]
  program_list[program_list[program_pointer+3]] = a + b
  return program_list

def run_mult_operation(program_list, program_pointer):
  a = program_list[program_list[program_pointer+1]]
  b = program_list[program_list[program_pointer+2]]
  program_list[program_list[program_pointer+3]] = a * b
  return program_list

def  run_operation_at_pointer(program_list, program_pointer):
  if(program_list[program_pointer] is ADD_OP_CODE):
    return run_add_operation(program_list, program_pointer)
  if(program_list[program_pointer] is MULT_OP_CODE):
    return run_mult_operation(program_list, program_pointer)

def  process_program(program_list, program_pointer):
  program_list = run_operation_at_pointer(program_list, program_pointer)
  program_pointer = program_pointer + 4
  print(program_list[program_pointer])
  if (program_list[program_pointer] is 99):
    return True
  else:
    process_program(program_list, program_pointer)

ammend_program()
process_program(program_list, program_pointer)

print(program_list)
