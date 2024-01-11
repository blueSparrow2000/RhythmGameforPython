'''
            ######### Type B: HHM climax

            for j in range(2):
                for i in range(2):
                    ### 흠 흐밍
                    pattern = basic_strike(beat_pos, 1, 1)
                    beat_pos += s1 - s16
                    f.write(pattern)

                    pattern = basic_strike(beat_pos, 2, 1)
                    beat_pos += s2
                    f.write(pattern)

                    pattern = basic_strike(beat_pos, 3, 1)
                    beat_pos += s2 + s4 + s16#s8
                    f.write(pattern)

                    ### 흠 흐 흠
                    pattern = basic_strike(beat_pos, 1, 1)
                    beat_pos += s2 + s4
                    f.write(pattern)

                    pattern = basic_strike(beat_pos, 2, 1)
                    beat_pos += s2 - s16
                    f.write(pattern)

                    pattern = basic_strike(beat_pos, 1, 1)
                    beat_pos += s1 - s8
                    f.write(pattern)

                    ### 흐
                    pattern = basic_strike(beat_pos, 2, 1)
                    beat_pos += s2 - s16
                    f.write(pattern)


                    if i==0:  # too late t16 or t32
                        beat_pos += s8 + s16
                        ### 밍밍밍
                        pattern = basic_hold(beat_pos, 3, 1, s1 - s16)
                        beat_pos += s1 + s2 + s4
                        f.write(pattern)

                    else:
                        ##########################
                        beat_pos += s4 + s16 + s32
                        ### 밍 흠
                        pattern = basic_strike(beat_pos, 3, 1)
                        beat_pos += s2 + s4 + s16
                        f.write(pattern)

                        pattern = basic_strike(beat_pos, 1, 1)
                        beat_pos += s1 - s8 - s16 - s32
                        f.write(pattern)


            ######### Type C: Hmm ming

            for k in range(2):
                for j in range(2):
                    for i in range(3):
                        pattern = basic_hold(beat_pos, 1, 1, t2)
                        beat_pos += t1
                        f.write(pattern)

                        pattern = basic_hold(beat_pos, 3, 1, t2)
                        beat_pos += t1
                        f.write(pattern)

                    if j==0:
                        pattern = basic_hold(beat_pos, 3, 1, t2)
                        beat_pos += t1
                        f.write(pattern)

                        pattern = basic_hold(beat_pos, 1, 1, t2)
                        beat_pos += t1
                        f.write(pattern)

                    elif j==1 and k==0:
                        pattern = basic_hold(beat_pos, 3, 1, t2)
                        beat_pos += t1
                        f.write(pattern)

                        beat_pos += t8- s16
                        pattern = basic_strike(beat_pos, 4, 1)
                        beat_pos += t1 - t8
                        f.write(pattern)

                        beat_pos += t32 # accuracy

                        # pattern = basic_hold(beat_pos, 4, 1, t4)
                        # beat_pos += t1
                        # f.write(pattern)

                    else: # j==1 and k==1
                        beat_pos += s16
                        for kk in range(2):
                            pattern = basic_strike(beat_pos, 1, 1)
                            beat_pos += t2 + 22
                            f.write(pattern)

                            pattern = basic_strike(beat_pos, 3, 1)
                            beat_pos += t2
                            f.write(pattern)

                            # pattern = basic_hold(beat_pos, 1, 1, t4)
                            # beat_pos += t2 - 4
                            # f.write(pattern)
                            #
                            # pattern = basic_hold(beat_pos, 3, 1, t4)
                            # beat_pos += t2 - 4
                            # f.write(pattern)

            beat_pos -= t16 # adjustment

            ######### Type D-1: Hmm ming ming

            pattern = basic_hold(beat_pos, 1, 1, t1)
            beat_pos += t1
            f.write(pattern)

            pattern = basic_strike(beat_pos, 2, 1)
            beat_pos += t2 - t8 - t16
            f.write(pattern)

            pattern = basic_strike(beat_pos, 3, 1)
            beat_pos += t2 + t4 + t32
            f.write(pattern)


            pattern = basic_strike(beat_pos, 1, 1)
            beat_pos += t2 - t32
            f.write(pattern)


            pattern = basic_strike(beat_pos, 2, 1)
            beat_pos += t2
            f.write(pattern)

            pattern = basic_strike(beat_pos, 3, 1)
            beat_pos += t2
            f.write(pattern)

            beat_pos += t2 + t4 - t8 # correction



            pattern = basic_hold(beat_pos, 1, 1, t1-t4)
            beat_pos += t1 - t8
            f.write(pattern)

            pattern = basic_strike(beat_pos, 2, 1)
            beat_pos += t2 - t16
            f.write(pattern)

            pattern = basic_strike(beat_pos, 3, 1)
            beat_pos += t2 + t4
            f.write(pattern)


            pattern = basic_hold(beat_pos, 1, 1, t1-t4)
            beat_pos += t1 - t8
            f.write(pattern)

            pattern = basic_strike(beat_pos, 2, 1)
            beat_pos += t2 - t16
            f.write(pattern)

            pattern = basic_strike(beat_pos, 3, 1)
            beat_pos += t1 + t2 + t16
            f.write(pattern)




            ######### Type D-2:
            pattern = basic_strike(beat_pos, 1, 1)
            beat_pos += 2*t1
            f.write(pattern)

            pattern = basic_strike(beat_pos, 1, 1)
            beat_pos += 2*t1
            f.write(pattern)

            pattern = basic_strike(beat_pos, 1, 1)
            beat_pos += 2*t1
            f.write(pattern)

            pattern = basic_strike(beat_pos - t16, 4, 1)
            beat_pos += t1
            f.write(pattern)


            for j in range(2):
                for i in range(3):
                    pattern = basic_hold(beat_pos, 1, 1, t2)
                    beat_pos += tex
                    f.write(pattern)

                    pattern = basic_hold(beat_pos, 3, 1, t2)
                    beat_pos += tex
                    f.write(pattern)

                if j==0:
                    pattern = basic_hold(beat_pos, 3, 1, t2)
                    beat_pos += tex
                    f.write(pattern)

                    pattern = basic_hold(beat_pos, 1, 1, t2)
                    beat_pos += tex
                    f.write(pattern)

                else:
                    pattern = basic_hold(beat_pos, 3, 1, t2)
                    beat_pos += tex
                    f.write(pattern)

                    pattern = basic_hold(beat_pos, 4, 1, t4)
                    beat_pos += tex
                    f.write(pattern)

                    # beat_pos += t8
                    # pattern = basic_strike(beat_pos, 4, 1)
                    # beat_pos += t1 - t8
                    # f.write(pattern)
            beat_pos -= t16 # adjustment

            ######## Type E: slow part + interlude

            for j in range(2):
                for i in range(2):
                    pattern = basic_hold(beat_pos, 1, 1, t2)
                    beat_pos += t1 - t8
                    f.write(pattern)

                    pattern = basic_strike(beat_pos, 3, 1)
                    beat_pos += e1
                    f.write(pattern)

                    pattern = basic_strike(beat_pos, 3, 1)
                    beat_pos += 3*e1
                    f.write(pattern)

                # ming hmm / hmm ming
                pattern = basic_strike(beat_pos, 3, 1)
                beat_pos += e3
                f.write(pattern)

                pattern = basic_strike(beat_pos, 1, 1)
                beat_pos += 3 * e1 + e3//2
                f.write(pattern)

                pattern = basic_strike(beat_pos, 1, 1)
                beat_pos += e3
                f.write(pattern)

                pattern = basic_strike(beat_pos, 3, 1)
                beat_pos += 4 * e1 + e1//4
                f.write(pattern)

            ### interlude
            beat_pos -= e1//2 - 100

            pattern = basic_strike(beat_pos, 4, 1)
            beat_pos += ee
            f.write(pattern)

            pattern = basic_strike(beat_pos, 4, 1)
            beat_pos += ee
            f.write(pattern)

            pattern = basic_strike(beat_pos, 4, 1)
            beat_pos += ee
            f.write(pattern)

            beat_pos += ee4

            pattern = basic_strike(beat_pos, 4, 1)
            beat_pos += ee4
            f.write(pattern)

            pattern = basic_strike(beat_pos, 4, 1)
            beat_pos += ee4
            f.write(pattern)

            pattern = basic_strike(beat_pos, 4, 1)
            beat_pos += ee4
            f.write(pattern)

            pattern = basic_strike(beat_pos, 4, 1)
            beat_pos += ee4*2
            f.write(pattern)

            # drum beats
            pattern = basic_strike(beat_pos, 4, 1)
            beat_pos += ee4*2
            f.write(pattern)

            pattern = basic_strike(beat_pos, 4, 1)
            beat_pos += ee4*2
            f.write(pattern)

            pattern = basic_strike(beat_pos, 4, 1)
            beat_pos += ee + ee//2 # - ee4//2
            f.write(pattern)

            # for i in range(6):
            #     pattern = basic_strike(beat_pos, 4, 1)
            #     beat_pos += ee4
            #     f.write(pattern)

            pattern = basic_hold(beat_pos, 4, 1, ee - 100)
            beat_pos += ee - ee4//2
            f.write(pattern)

            # for i in range(6):
            #     pattern = basic_strike(beat_pos, 4, 1)
            #     beat_pos += ee4//2
            #     f.write(pattern)

            # for i in range(4):
            #     pattern = basic_strike(beat_pos, 2, 1)
            #     beat_pos += ee4//4
            #     f.write(pattern)
            #     pattern = basic_strike(beat_pos, 3, 1)
            #     beat_pos += ee4//4
            #     f.write(pattern)

            beat_pos += ee//4 - 100 # 200# adjustment


            ######### Type B
            for j in range(2):
                for i in range(2):
                    ### 흠 흐밍
                    pattern = basic_strike(beat_pos, 1, 1)
                    beat_pos += s1 - s16
                    f.write(pattern)

                    pattern = basic_strike(beat_pos, 2, 1)
                    beat_pos += s2
                    f.write(pattern)

                    pattern = basic_strike(beat_pos, 3, 1)
                    beat_pos += s2 + s4 + s16  # s8
                    f.write(pattern)

                    ### 흠 흐 흠
                    pattern = basic_strike(beat_pos, 1, 1)
                    beat_pos += s2 + s4
                    f.write(pattern)

                    pattern = basic_strike(beat_pos, 2, 1)
                    beat_pos += s2 - s16
                    f.write(pattern)

                    pattern = basic_strike(beat_pos, 1, 1)
                    beat_pos += s1 - s8
                    f.write(pattern)

                    ### 흐
                    pattern = basic_strike(beat_pos, 2, 1)
                    beat_pos += s2 - s16
                    f.write(pattern)

                    if i == 0:  # too late t16 or t32
                        beat_pos += s8 + s16
                        ### 밍밍밍
                        pattern = basic_hold(beat_pos, 3, 1, s1 - s16)
                        beat_pos += s1 + s2 + s4
                        f.write(pattern)

                    else:
                        ##########################
                        beat_pos += s4 + s16 + s32
                        ### 밍 흠
                        pattern = basic_strike(beat_pos, 3, 1)
                        beat_pos += s2 + s4 + s16
                        f.write(pattern)

                        pattern = basic_strike(beat_pos, 1, 1)
                        beat_pos += s1 - s8 - s16 - s32
                        f.write(pattern)

            beat_pos += 0 # adjustment

            ######### Type B
            for j in range(2):
                for i in range(2):
                    ### 흠 흐밍
                    pattern = basic_strike(beat_pos, 1, 1)
                    beat_pos += s1 - s16
                    f.write(pattern)

                    pattern = basic_strike(beat_pos, 2, 1)
                    beat_pos += s2
                    f.write(pattern)

                    pattern = basic_strike(beat_pos, 3, 1)
                    beat_pos += s2 + s4 + s16  # s8
                    f.write(pattern)

                    ### 흠 흐 흠
                    pattern = basic_strike(beat_pos, 1, 1)
                    beat_pos += s2 + s4
                    f.write(pattern)

                    pattern = basic_strike(beat_pos, 2, 1)
                    beat_pos += s2 - s16
                    f.write(pattern)

                    pattern = basic_strike(beat_pos, 1, 1)
                    beat_pos += s1 - s8
                    f.write(pattern)

                    ### 흐
                    pattern = basic_strike(beat_pos, 2, 1)
                    beat_pos += s2 - s16
                    f.write(pattern)

                    if i == 0:  # too late t16 or t32
                        beat_pos += s8 + s16
                        ### 밍밍밍
                        pattern = basic_hold(beat_pos, 3, 1, s1 - s16)
                        beat_pos += s1 + s2 + s4
                        f.write(pattern)

                    else:
                        ##########################
                        beat_pos += s4 + s16 + s32
                        ### 밍 흠
                        pattern = basic_strike(beat_pos, 3, 1)
                        beat_pos += s2 + s4 + s16
                        f.write(pattern)

                        pattern = basic_strike(beat_pos, 1, 1)
                        beat_pos += s1 - s8 - s16 - s32
                        f.write(pattern)

            beat_pos += 0  # adjustment

            ######### Type A


'''
