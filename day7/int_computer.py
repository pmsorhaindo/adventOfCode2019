# op codes
ADD_OP_CODE = 1
MULT_OP_CODE = 2
INPUT_OP_CODE = 3
OUTPUT_OP_CODE = 4
JMP_IF_TRUE_OP_CODE = 5
JMP_IF_FALSE_OP_CODE = 6
LESS_THAN_OP_CODE = 7
EQUALS_OPCODE = 8

class IntComputer:
  """IntComputer instance"""

  def __init__(self, phase):
    self.code = self.load_program()
    self.phase_set = False
    self.phase = phase
    self.awaiting_input = False
    self.output = None
    self.complete = False
    self.load_point = 0
    self.input_signal = 0
    self.run()

  def load_program(self):
    f = open('input.txt')
    line = f.readline()
    return [int(s) for s in line.split(',')]

  def run_add_operation(self, program_list, instruction_pointer, parsed_instruction):
    a = program_list[program_list[instruction_pointer+1]] if int(parsed_instruction[2]) == 0 else program_list[instruction_pointer+1]
    b = program_list[program_list[instruction_pointer+2]] if int(parsed_instruction[1]) == 0 else program_list[instruction_pointer+2]
    program_list[program_list[instruction_pointer+3]] = a + b
    return (program_list, 4, False)

  def run_mult_operation(self, program_list, instruction_pointer, parsed_instruction):
    a = program_list[program_list[instruction_pointer+1]] if int(parsed_instruction[2]) == 0 else program_list[instruction_pointer+1]
    b = program_list[program_list[instruction_pointer+2]] if int(parsed_instruction[1]) == 0 else program_list[instruction_pointer+2]
    program_list[program_list[instruction_pointer+3]] = a * b
    return (program_list, 4, False)

  def run_input_operation(self, program_list, instruction_pointer, parsed_instruction):
    print('set phase  for ', self.phase)
    if self.phase_set == False:
      program_list[program_list[instruction_pointer+1]] = self.phase
      self.phase_set = True
      self.awaiting_input = False
      return (program_list, 2, False)
    else:
      print('input for', self.phase)
      if self.awaiting_input:
        self.load_point = [instruction_pointer]
        return (program_list, 0, False)
      else:
        print('preceeding from input')
        program_list[program_list[instruction_pointer+1]] = self.input_signal
        self.awaiting_input = True
        return (program_list, 2, False)

  def run_output_operation(self, program_list, instruction_pointer, parsed_instruction):
    print(self.phase, '>>', program_list[program_list[instruction_pointer+1]])
    self.output = program_list[program_list[instruction_pointer+1]] 
    return (program_list, 2, False)

  def run_if_true_operation(self, program_list, instruction_pointer, parsed_instruction):
    condition = program_list[program_list[instruction_pointer+1]] if int(parsed_instruction[2]) == 0 else program_list[instruction_pointer+1]
    location = program_list[program_list[instruction_pointer+2]] if int(parsed_instruction[1]) == 0 else program_list[instruction_pointer+2]
    if condition != 0:
      return (program_list, location, True)
    return (program_list, 3, False)

  def run_if_false_operation(self, program_list, instruction_pointer, parsed_instruction):
    condition = program_list[program_list[instruction_pointer+1]] if int(parsed_instruction[2]) == 0 else program_list[instruction_pointer+1]
    location = program_list[program_list[instruction_pointer+2]] if int(parsed_instruction[1]) == 0 else program_list[instruction_pointer+2]
    if condition == 0:
      return (program_list, location, True)
    return (program_list, 3, False)

  def run_if_less_operation(self, program_list, instruction_pointer, parsed_instruction):
    first = program_list[program_list[instruction_pointer+1]] if int(parsed_instruction[2]) == 0 else program_list[instruction_pointer+1]
    second = program_list[program_list[instruction_pointer+2]] if int(parsed_instruction[1]) == 0 else program_list[instruction_pointer+2]
    if first < second:
      if int(parsed_instruction[0]) == 0:
        program_list[program_list[instruction_pointer+3]] = 1
      else:
        program_list[instruction_pointer+3] = 1
    else:
      if int(parsed_instruction[0]) == 0:
        program_list[program_list[instruction_pointer+3]] = 0
      else:
        program_list[instruction_pointer+3] = 0
    return (program_list, 4, False)

  def run_if_equal_operation(self, program_list, instruction_pointer, parsed_instruction):
    first = program_list[program_list[instruction_pointer+1]] if int(parsed_instruction[2]) == 0 else program_list[instruction_pointer+1]
    second = program_list[program_list[instruction_pointer+2]] if int(parsed_instruction[1]) == 0 else program_list[instruction_pointer+2]
    print(first, second, program_list[program_list[instruction_pointer+3]], parsed_instruction[0], program_list)
    if first == second:
      if int(parsed_instruction[0]) == 0:
        program_list[program_list[instruction_pointer+3]] = 1
      else:
        program_list[instruction_pointer+3] = 1
    else:
      if int(parsed_instruction[0]) == 0:
        program_list[program_list[instruction_pointer+3]] = 0
      else:
        program_list[instruction_pointer+3] = 0
    return (program_list, 4, False)

  def run_operation_at_pointer(self, program_list, instruction_pointer):
    parsed_instruction = list(str(program_list[instruction_pointer]))
    while len(parsed_instruction) != 5:
      parsed_instruction.insert(0,0)
    if(program_list[instruction_pointer] % 100 is ADD_OP_CODE):
      return self.run_add_operation(program_list, instruction_pointer, parsed_instruction)
    if(program_list[instruction_pointer] % 100 is MULT_OP_CODE):
      return self.run_mult_operation(program_list, instruction_pointer, parsed_instruction)
    if(program_list[instruction_pointer] % 100 is INPUT_OP_CODE):
      return self.run_input_operation(program_list, instruction_pointer, parsed_instruction)
    if(program_list[instruction_pointer] % 100 is OUTPUT_OP_CODE):
      return self.run_output_operation(program_list, instruction_pointer, parsed_instruction)
    if(program_list[instruction_pointer] % 100 is JMP_IF_TRUE_OP_CODE):
      return self.run_if_true_operation(program_list, instruction_pointer, parsed_instruction)
    if(program_list[instruction_pointer] % 100 is JMP_IF_FALSE_OP_CODE):
      return self.run_if_false_operation(program_list, instruction_pointer, parsed_instruction)
    if(program_list[instruction_pointer] % 100 is LESS_THAN_OP_CODE):
      return self.run_if_less_operation(program_list, instruction_pointer, parsed_instruction)
    if(program_list[instruction_pointer] % 100 is EQUALS_OPCODE):
      return self.run_if_equal_operation(program_list, instruction_pointer, parsed_instruction)

  def process_program(self, program_list, instruction_pointer):
    program_list, param_jump, absolute_jump = self.run_operation_at_pointer(program_list, instruction_pointer)

    if absolute_jump:
      instruction_pointer = param_jump
    else:
      instruction_pointer = instruction_pointer + param_jump

    if self.awaiting_input and program_list[instruction_pointer] % 100 is INPUT_OP_CODE:
      print('terminating')
      return self.output

    if (program_list[instruction_pointer] is 99):
      self.complete = True
      return program_list[0]
    else:
      return self.process_program(program_list, instruction_pointer)

  def run(self):
    print('process', self.phase, 'from', self.load_point)
    self.process_program(self.code, self.load_point)
    print('getting', self.output)
    return self.output

  def input(self, input_signal):
    self.input_signal = input_signal
    self.awaiting_input = False
