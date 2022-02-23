


def generate(x):
    from magenta.models.melody_rnn import melody_rnn_generate
    melody_rnn_generate.main.config="basic_rnn"
    melody_rnn_generate.FLAGS.bundle_file="basic_rnn.mag"
    melody_rnn_generate.FLAGS.output_dir="./tmp/melody_rnn/generated"
    melody_rnn_generate.FLAGS.num_outputs=1
    melody_rnn_generate.FLAGS.num_steps=150
    melody_rnn_generate.FLAGS.primer_midi="./uploads/"+x
    melody_rnn_generate.console_entry_point()

def add(a,b):
    c=a+b
    
add(4,5)
generate("2.mid")