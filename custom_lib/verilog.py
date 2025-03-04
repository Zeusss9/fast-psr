import numpy as np

def create_tb(max_bitwidth, min_bitwidth, fixedpoint_bit_width, config):
    txt_file = open('../verilog/TB_QEA.v')
    data = txt_file.readlines()
    txt_file.close()

    tb_path = '../verilog/'

    for bit_temp in range(min_bitwidth, max_bitwidth + 1):
        if(config.clipping_flag):
            tb_verilog = open(tb_path + str(bit_temp) + '_bits/TestBench_MPQNN_Pilot_' + str(config.num_pilot) + '_QAM_' + str(config.QAM_mod) + '_SNR_' + str(config.SNRdB) + '_' + str(config.num_tx_antenna) + 'x' + str(config.num_rx_antenna) + "_" + str(round(20*np.log10(config.CR))) + 'dB_' + str(bit_temp) + '_bits.v', mode='w')
        else:
            tb_verilog = open(tb_path + str(bit_temp) + '_bits/TestBench_MPQNN_Pilot_' + str(config.num_pilot) + '_QAM_' + str(config.QAM_mod) + '_SNR_' + str(config.SNRdB) + '_' + str(config.num_tx_antenna) + 'x' + str(config.num_rx_antenna) + '_' + str(bit_temp) + '_bits.v', mode='w')

        if(config.clipping_flag):
            for j in range(len(data)):
                if(j == 2):
                    tb_verilog.write('module TestBench_MPQNN_Pilot_' + str(config.num_pilot) + '_QAM_' + str(config.QAM_mod) + '_SNR_' + str(config.SNRdB) + '_' + str(config.num_tx_antenna) + 'x' + str(config.num_rx_antenna) + "_" + str(round(20*np.log10(config.CR))) + 'dB_' + str(bit_temp) + '_bits();\n')
                elif(j == 3):
                    tb_verilog.write('    parameter FIXED_POINT_WIDTH = ' + str(fixedpoint_bit_width) + ';\n')
                elif(j == 4):
                    tb_verilog.write('    parameter BIT_WIDTH = ' + str(bit_temp) + ';\n')
                elif(j == 6):
                    tb_verilog.write('    parameter LINK_Input_0 = "..\\\\..\\\\txt_file\\\\Layer\\\\Input_verilog_0_Pilot_' + str(config.num_pilot) + '_QAM_' + str(config.QAM_mod) + '_SNR_' + str(config.SNRdB) + '_' + str(config.num_tx_antenna) + 'x' + str(config.num_rx_antenna) + "_" + str(round(20*np.log10(config.CR))) + 'dB_' + str(bit_temp) + '_bits.txt' + '";\n')
                elif(j == 7):
                    tb_verilog.write('    parameter LINK_Input_1 = "..\\\\..\\\\txt_file\\\\Layer\\\\Input_verilog_1_Pilot_' + str(config.num_pilot) + '_QAM_' + str(config.QAM_mod) + '_SNR_' + str(config.SNRdB) + '_' + str(config.num_tx_antenna) + 'x' + str(config.num_rx_antenna) + "_" + str(round(20*np.log10(config.CR))) + 'dB_' + str(bit_temp) + '_bits.txt' + '";\n')
                elif(j == 8):
                    tb_verilog.write('    parameter LINK_Hidden_0 = "..\\\\..\\\\txt_file\\\\Layer\\\\Hidden_0_Pilot_' + str(config.num_pilot) + '_QAM_' + str(config.QAM_mod) + '_SNR_' + str(config.SNRdB) + '_' + str(config.num_tx_antenna) + 'x' + str(config.num_rx_antenna) + "_" + str(round(20*np.log10(config.CR))) + 'dB_' + str(bit_temp) + '_bits.txt' + '";\n')
                elif(j == 9):
                    tb_verilog.write('    parameter LINK_Hidden_1 = "..\\\\..\\\\txt_file\\\\Layer\\\\Hidden_1_Pilot_' + str(config.num_pilot) + '_QAM_' + str(config.QAM_mod) + '_SNR_' + str(config.SNRdB) + '_' + str(config.num_tx_antenna) + 'x' + str(config.num_rx_antenna) + "_" + str(round(20*np.log10(config.CR))) + 'dB_' + str(bit_temp) + '_bits.txt' + '";\n')
                elif(j == 10):
                    tb_verilog.write('    parameter LINK_Hidden_2 = "..\\\\..\\\\txt_file\\\\Layer\\\\Hidden_2_Pilot_' + str(config.num_pilot) + '_QAM_' + str(config.QAM_mod) + '_SNR_' + str(config.SNRdB) + '_' + str(config.num_tx_antenna) + 'x' + str(config.num_rx_antenna) + "_" + str(round(20*np.log10(config.CR))) + 'dB_' + str(bit_temp) + '_bits.txt' + '";\n')
                elif(j == 11):
                    tb_verilog.write('    parameter LINK_Output = "..\\\\..\\\\txt_file\\\\Layer\\\\Output_Pilot_' + str(config.num_pilot) + '_QAM_' + str(config.QAM_mod) + '_SNR_' + str(config.SNRdB) + '_' + str(config.num_tx_antenna) + 'x' + str(config.num_rx_antenna) + "_" + str(round(20*np.log10(config.CR))) + 'dB_' + str(bit_temp) + '_bits.txt' + '";\n')
                elif(j == 12):
                    tb_verilog.write('    parameter LINK_W1 = "..\\\\..\\\\txt_file\\\\Weight\\\\W1_verilog_Pilot_' + str(config.num_pilot) + '_QAM_' + str(config.QAM_mod) + '_SNR_' + str(config.SNRdB) + '_' + str(config.num_tx_antenna) + 'x' + str(config.num_rx_antenna) + "_" + str(round(20*np.log10(config.CR))) + 'dB_' + str(bit_temp) + '_bits.txt' + '";\n')
                elif(j == 13):
                    tb_verilog.write('    parameter LINK_W2 = "..\\\\..\\\\txt_file\\\\Weight\\\\W2_verilog_Pilot_' + str(config.num_pilot) + '_QAM_' + str(config.QAM_mod) + '_SNR_' + str(config.SNRdB) + '_' + str(config.num_tx_antenna) + 'x' + str(config.num_rx_antenna) + "_" + str(round(20*np.log10(config.CR))) + 'dB_' + str(bit_temp) + '_bits.txt' + '";\n')
                elif(j == 14):
                    tb_verilog.write('    parameter LINK_W3 = "..\\\\..\\\\txt_file\\\\Weight\\\\W3_verilog_Pilot_' + str(config.num_pilot) + '_QAM_' + str(config.QAM_mod) + '_SNR_' + str(config.SNRdB) + '_' + str(config.num_tx_antenna) + 'x' + str(config.num_rx_antenna) + "_" + str(round(20*np.log10(config.CR))) + 'dB_' + str(bit_temp) + '_bits.txt' + '";\n')
                elif(j == 15):
                    tb_verilog.write('    parameter LINK_W4 = "..\\\\..\\\\txt_file\\\\Weight\\\\W4_verilog_Pilot_' + str(config.num_pilot) + '_QAM_' + str(config.QAM_mod) + '_SNR_' + str(config.SNRdB) + '_' + str(config.num_tx_antenna) + 'x' + str(config.num_rx_antenna) + "_" + str(round(20*np.log10(config.CR))) + 'dB_' + str(bit_temp) + '_bits.txt' + '";\n')
                elif(j == 16):
                    tb_verilog.write('    parameter LINK_B1 = "..\\\\..\\\\txt_file\\\\Bias\\\\B1_verilog_Pilot_' + str(config.num_pilot) + '_QAM_' + str(config.QAM_mod) + '_SNR_' + str(config.SNRdB) + '_' + str(config.num_tx_antenna) + 'x' + str(config.num_rx_antenna) + "_" + str(round(20*np.log10(config.CR))) + 'dB_' + str(bit_temp) + '_bits.txt' + '";\n')
                elif(j == 17):
                    tb_verilog.write('    parameter LINK_B2 = "..\\\\..\\\\txt_file\\\\Bias\\\\B2_verilog_Pilot_' + str(config.num_pilot) + '_QAM_' + str(config.QAM_mod) + '_SNR_' + str(config.SNRdB) + '_' + str(config.num_tx_antenna) + 'x' + str(config.num_rx_antenna) + "_" + str(round(20*np.log10(config.CR))) + 'dB_' + str(bit_temp) + '_bits.txt' + '";\n')
                elif(j == 18):
                    tb_verilog.write('    parameter LINK_B3 = "..\\\\..\\\\txt_file\\\\Bias\\\\B3_verilog_Pilot_' + str(config.num_pilot) + '_QAM_' + str(config.QAM_mod) + '_SNR_' + str(config.SNRdB) + '_' + str(config.num_tx_antenna) + 'x' + str(config.num_rx_antenna) + "_" + str(round(20*np.log10(config.CR))) + 'dB_' + str(bit_temp) + '_bits.txt' + '";\n')
                elif(j == 19):
                    tb_verilog.write('    parameter LINK_B4 = "..\\\\..\\\\txt_file\\\\Bias\\\\B4_verilog_Pilot_' + str(config.num_pilot) + '_QAM_' + str(config.QAM_mod) + '_SNR_' + str(config.SNRdB) + '_' + str(config.num_tx_antenna) + 'x' + str(config.num_rx_antenna) + "_" + str(round(20*np.log10(config.CR))) + 'dB_' + str(bit_temp) + '_bits.txt' + '";\n')
                elif(j == 144):
                    tb_verilog.write('    QNN_Pilot_' + str(config.num_pilot) + '_QAM_' + str(config.QAM_mod) + '_SNR_' + str(config.SNRdB) + '_' + str(config.num_tx_antenna) + 'x' + str(config.num_rx_antenna) + "_" + str(round(20*np.log10(config.CR))) + 'dB_' + str(bit_temp) + '_bits\n')
                else:
                    tb_verilog.write(data[j])
        else:
            for j in range(len(data)):
                if(j == 2):
                    tb_verilog.write('module TestBench_MPQNN_Pilot_' + str(config.num_pilot) + '_QAM_' + str(config.QAM_mod) + '_SNR_' + str(config.SNRdB) + '_' + str(config.num_tx_antenna) + 'x' + str(config.num_rx_antenna) + "_" + str(bit_temp) + '_bits();\n')
                elif(j == 3):
                    tb_verilog.write('    parameter FIXED_POINT_WIDTH = ' + str(fixedpoint_bit_width) + ';\n')
                elif(j == 4):
                    tb_verilog.write('    parameter BIT_WIDTH = ' + str(bit_temp) + ';\n')
                elif(j == 6):
                    tb_verilog.write('    parameter LINK_Input_0 = "..\\\\..\\\\txt_file\\\\Layer\\\\Input_verilog_0_Pilot_' + str(config.num_pilot) + '_QAM_' + str(config.QAM_mod) + '_SNR_' + str(config.SNRdB) + '_' + str(config.num_tx_antenna) + 'x' + str(config.num_rx_antenna) + "_" + str(bit_temp) + '_bits.txt' + '";\n')
                elif(j == 7):
                    tb_verilog.write('    parameter LINK_Input_1 = "..\\\\..\\\\txt_file\\\\Layer\\\\Input_verilog_1_Pilot_' + str(config.num_pilot) + '_QAM_' + str(config.QAM_mod) + '_SNR_' + str(config.SNRdB) + '_' + str(config.num_tx_antenna) + 'x' + str(config.num_rx_antenna) + "_" + str(bit_temp) + '_bits.txt' + '";\n')
                elif(j == 8):
                    tb_verilog.write('    parameter LINK_Hidden_0 = "..\\\\..\\\\txt_file\\\\Layer\\\\Hidden_0_Pilot_' + str(config.num_pilot) + '_QAM_' + str(config.QAM_mod) + '_SNR_' + str(config.SNRdB) + '_' + str(config.num_tx_antenna) + 'x' + str(config.num_rx_antenna) + "_" + str(bit_temp) + '_bits.txt' + '";\n')
                elif(j == 9):
                    tb_verilog.write('    parameter LINK_Hidden_1 = "..\\\\..\\\\txt_file\\\\Layer\\\\Hidden_1_Pilot_' + str(config.num_pilot) + '_QAM_' + str(config.QAM_mod) + '_SNR_' + str(config.SNRdB) + '_' + str(config.num_tx_antenna) + 'x' + str(config.num_rx_antenna) + "_" + str(bit_temp) + '_bits.txt' + '";\n')
                elif(j == 10):
                    tb_verilog.write('    parameter LINK_Hidden_2 = "..\\\\..\\\\txt_file\\\\Layer\\\\Hidden_2_Pilot_' + str(config.num_pilot) + '_QAM_' + str(config.QAM_mod) + '_SNR_' + str(config.SNRdB) + '_' + str(config.num_tx_antenna) + 'x' + str(config.num_rx_antenna) + "_" + str(bit_temp) + '_bits.txt' + '";\n')
                elif(j == 11):
                    tb_verilog.write('    parameter LINK_Output = "..\\\\..\\\\txt_file\\\\Layer\\\\Output_Pilot_' + str(config.num_pilot) + '_QAM_' + str(config.QAM_mod) + '_SNR_' + str(config.SNRdB) + '_' + str(config.num_tx_antenna) + 'x' + str(config.num_rx_antenna) + "_" + str(bit_temp) + '_bits.txt' + '";\n')
                elif(j == 12):
                    tb_verilog.write('    parameter LINK_W1 = "..\\\\..\\\\txt_file\\\\Weight\\\\W1_verilog_Pilot_' + str(config.num_pilot) + '_QAM_' + str(config.QAM_mod) + '_SNR_' + str(config.SNRdB) + '_' + str(config.num_tx_antenna) + 'x' + str(config.num_rx_antenna) + "_" + str(bit_temp) + '_bits.txt' + '";\n')
                elif(j == 13):
                    tb_verilog.write('    parameter LINK_W2 = "..\\\\..\\\\txt_file\\\\Weight\\\\W2_verilog_Pilot_' + str(config.num_pilot) + '_QAM_' + str(config.QAM_mod) + '_SNR_' + str(config.SNRdB) + '_' + str(config.num_tx_antenna) + 'x' + str(config.num_rx_antenna) + "_" + str(bit_temp) + '_bits.txt' + '";\n')
                elif(j == 14):
                    tb_verilog.write('    parameter LINK_W3 = "..\\\\..\\\\txt_file\\\\Weight\\\\W3_verilog_Pilot_' + str(config.num_pilot) + '_QAM_' + str(config.QAM_mod) + '_SNR_' + str(config.SNRdB) + '_' + str(config.num_tx_antenna) + 'x' + str(config.num_rx_antenna) + "_" + str(bit_temp) + '_bits.txt' + '";\n')
                elif(j == 15):
                    tb_verilog.write('    parameter LINK_W4 = "..\\\\..\\\\txt_file\\\\Weight\\\\W4_verilog_Pilot_' + str(config.num_pilot) + '_QAM_' + str(config.QAM_mod) + '_SNR_' + str(config.SNRdB) + '_' + str(config.num_tx_antenna) + 'x' + str(config.num_rx_antenna) + "_" + str(bit_temp) + '_bits.txt' + '";\n')
                elif(j == 16):
                    tb_verilog.write('    parameter LINK_B1 = "..\\\\..\\\\txt_file\\\\Bias\\\\B1_verilog_Pilot_' + str(config.num_pilot) + '_QAM_' + str(config.QAM_mod) + '_SNR_' + str(config.SNRdB) + '_' + str(config.num_tx_antenna) + 'x' + str(config.num_rx_antenna) + "_" + str(bit_temp) + '_bits.txt' + '";\n')
                elif(j == 17):
                    tb_verilog.write('    parameter LINK_B2 = "..\\\\..\\\\txt_file\\\\Bias\\\\B2_verilog_Pilot_' + str(config.num_pilot) + '_QAM_' + str(config.QAM_mod) + '_SNR_' + str(config.SNRdB) + '_' + str(config.num_tx_antenna) + 'x' + str(config.num_rx_antenna) + "_" + str(bit_temp) + '_bits.txt' + '";\n')
                elif(j == 18):
                    tb_verilog.write('    parameter LINK_B3 = "..\\\\..\\\\txt_file\\\\Bias\\\\B3_verilog_Pilot_' + str(config.num_pilot) + '_QAM_' + str(config.QAM_mod) + '_SNR_' + str(config.SNRdB) + '_' + str(config.num_tx_antenna) + 'x' + str(config.num_rx_antenna) + "_" + str(bit_temp) + '_bits.txt' + '";\n')
                elif(j == 19):
                    tb_verilog.write('    parameter LINK_B4 = "..\\\\..\\\\txt_file\\\\Bias\\\\B4_verilog_Pilot_' + str(config.num_pilot) + '_QAM_' + str(config.QAM_mod) + '_SNR_' + str(config.SNRdB) + '_' + str(config.num_tx_antenna) + 'x' + str(config.num_rx_antenna) + "_" + str(bit_temp) + '_bits.txt' + '";\n')
                elif(j == 144):
                    tb_verilog.write('    QNN_Pilot_' + str(config.num_pilot) + '_QAM_' + str(config.QAM_mod) + '_SNR_' + str(config.SNRdB) + '_' + str(config.num_tx_antenna) + 'x' + str(config.num_rx_antenna) + "_" + str(bit_temp) + '_bits\n')
                else:
                    tb_verilog.write(data[j])

        tb_verilog.close()
