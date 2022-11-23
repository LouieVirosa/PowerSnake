"""
Everything you need to create your own POWERSNAKE challenge!

The challenge:

Given a block of multi-line ascii text where the characters all look like snakes,
find the encoded lat/lon.

The encoding rules are as follows:

1) A line can encode at most 1 digit of the answer.
2) If a line encodes 1 digit of the answer IFF the line above it contains exactly 31 slashes ("\"s and "/"s)
3) The digit encoded is found by the number of "1"s in a line minus the number of "l"s. 


"""
from collections import Counter
import random

snake_chars = ['|', 'I', 'l', '1', '\\', '/']
encoded_lat = "N 38 43.249" # Just for testing... not valid! Good thought looking
encoded_lon = "W 77 22.592" # At old commits though!

def encoded_line_marker(line_length=80):
  num_fwd_slashes = random.randint(1,31)
  num_back_slashes = 31 - num_fwd_slashes
  remaining_chars = ['|', 'I', 'l', '1']
  raw_str = ("/" * num_fwd_slashes) + ("\\" * num_back_slashes)
  while len(raw_str) < line_length:
    raw_str += random.choice(remaining_chars)
  mylist = list(raw_str)
  random.shuffle(mylist)
  return ''.join(mylist)


def encode_line(num_to_encode, line_length=80):
  num_ls = random.randint(1,12)
  num_ones = int(num_to_encode) + num_ls
  num_fwd_slashes = random.randint(1,15)
  num_back_slashes = random.randint(1,15)
  raw_string = ("l" * num_ls) + ("1" * num_ones) + ("/" * num_fwd_slashes) + ("\\" * num_back_slashes)
  raw_string += ("|" * (line_length - len(raw_string)))
  mylist = list(raw_string)
  random.shuffle(mylist)
  return ''.join(mylist)
  
  
def gen_puzzle():
  enc_lat = ''.join([s for s in encoded_lat if s.isdigit()])
  enc_lon = ''.join([s for s in encoded_lon if s.isdigit()])
  enc_msg = enc_lat + enc_lon
  
  puzzle = []
  for num in enc_msg:
    # prepend some garbage
    for prepend_line in range(0, random.randint(0,10)):
      while True:
        line = ""                                                                                                                                                                                                   
        for char in range(80):                                                                                                                                                                                      
          line += random.choice(snake_chars)
        if not test_encoded_line(line):
          break
      assert not test_encoded_line(line)
      assert len(line) == 80
      puzzle.append(line + "\tGARBAGE")
      
    # put an encoding line
    line = encoded_line_marker()
    assert test_encoded_line(line)
    assert len(line) == 80
    puzzle.append(line + "\tMARKER")
    
    line = encode_line(num)
    assert not test_encoded_line(line)
    assert len(line) == 80
    puzzle.append(line  + f"\tENCODED: {num}")
    
    # postpend some garbage
    for postpend_line in range(0, random.randint(0,10)):
      while True:
        line = ""                                                                                                                                                                                                   
        for char in range(80):                                                                                                                                                                                      
          line += random.choice(snake_chars)
        if not test_encoded_line(line):
          break
      assert not test_encoded_line(line)
      assert len(line) == 80
      puzzle.append(line + "\tGARBAGE")
      
  # print puzzle
  for line in puzzle:
    print(line)
    
    
  


def test_encoded_line(line):
  """
  Returns True IFF the number of slashes in the line add up to 31
  """
  counts = Counter(line)
  return counts["/"] + counts["\\"] == 31
  

if __name__ == "__main__":
     gen_puzzle()
