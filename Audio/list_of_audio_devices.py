import speech_recognition as s_r
print('List of Audio devices')
print(s_r.Microphone.list_microphone_names())


#sample output
'''
['Microsoft Sound Mapper - Input', 'External Microphone (Realtek(R)', 'Microphone (Realtek(R) Audio)',
 'Microsoft Sound Mapper - Output', 'Headphones (Realtek(R) Audio)', 'Speakers (Realtek(R) Audio)']

'''