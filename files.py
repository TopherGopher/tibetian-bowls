import os

print 'var sounds = [\n'
for (dirpath, dirnames, filenames) in os.walk("tibetian"):
    for filename in filenames:
	if ".wav" in filename:
		file_without_extension = filename.split(".wav")[0]
		full_file_path = "%s/%s" % (dirpath, file_without_extension)
		#print 'var %s = new buzz.sound("%s", {formats: ["wav"]});' % (file_without_extension, full_file_path)	
		print 'new buzz.sound("%s", {formats: ["wav"]}),' % full_file_path
		

print '];'
