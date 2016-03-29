# from obspy import read
# import obspy.imaging
#
# st = read('NZKHZ__LHN10.sac')
# print(st)
# tr = st[0]
# print(tr)
# st.plot(color='gray', tick_format='%I:%M %p', starttime=st[0].stats.starttime, endtime=st[0].stats.starttime+432000)
# st[0].spectrogram(log=True)

# from neo import io
# import codecs
#
#
# with codecs.open('temp/akshay.eeg', "r",encoding='utf-8', errors='ignore') as fdata:
#     for x in fdata:
#         print(x)


# r = io.BrainVisionIO( filename = 'temp/akshay.eeg')
#
# seg = r.read_segment(lazy = False, cascade = True,)
