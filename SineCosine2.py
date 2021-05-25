from manim import *
import numpy as np






class axesConstruction(Scene):

      def construct(self):
          
          a = 0


############ Axes setup ########################################

          dot = Dot(radius = 0.05,color =BLUE)
          numberplane = NumberPlane( x_range=[-7.111111111111111,7.111111111111111,2 ], y_range=[-4.0, 4.0, 2])
           
          
############ Axes setup ends ########################################
               
           
     

########################### ValueTrackers start #################################################################           
          

          theta = ValueTracker(0.001)



########################### ValueTrackers end #################################################################           
          

################################################## vectors start ###################################################################################################

          arrow_moving1 = Arrow(ORIGIN, [2*np.cos(theta.get_value()*DEGREES),2*np.sin(theta.get_value()*DEGREES),0], buff = 0, color = PURPLE) 
          arrow_moving2 = Arrow(ORIGIN,[4*np.cos(theta.get_value()*DEGREES),4*np.sin(theta.get_value()*DEGREES),0], buff = 0, color = PURPLE )
          arrow_moving3 = Arrow(ORIGIN,[np.cos(theta.get_value()*DEGREES),np.sin(theta.get_value()*DEGREES),0], buff = 0, color = PURPLE )
          
          sine = Arrow([2*np.cos(theta.get_value()*DEGREES),0,0], [2*np.cos(theta.get_value()*DEGREES),2*np.sin(theta.get_value()*DEGREES),0], buff = 0, color = ORANGE) 
          cosine = Arrow(ORIGIN, [2*np.cos(theta.get_value()*DEGREES),0,0], buff = 0, color = YELLOW) 


################################################### vectors end #####################################################################################################







################### elements necessary for rotation and not displayed on screen start  ############################## 

        

          line_still = Line([0,0,0],[2,0,0])
          line_moving = Line([0,0,0],[np.cos(theta.get_value()*DEGREES),np.sin(theta.get_value()*DEGREES),0],color = PURPLE)



################### elements necessary for rotation and not displayed on screen end ############################## 





############### angles start  #########################


          a = Angle(line_still, line_moving, radius=0.25, other_angle=False)


############### angles end  #########################


###############################  texts start ##########################################################################

          text = MathTex(r"\theta")
          text.scale(0.6)
          theta_symbol =text.move_to(Angle(line_still, line_moving, radius=0.25 + 3 * SMALL_BUFF, other_angle=False).point_from_proportion(0.5))
           
          text_sine = MathTex(r"sin(\theta)") 
          text_sine.scale(0.58)
          text_sine.set_color(ORANGE)
          sin_theta_symbol = text_sine.move_to(sine.get_center() + 0.5*RIGHT)

          text_cos = MathTex(r"cos(\theta)") 
          text_cos.scale(0.58)
          text_cos.set_color(YELLOW)
          cos_theta_symbol = text_cos.move_to(cosine.get_center() + 0.5*DOWN)


###############################  texts end ##############################################################################################     

     
####################### updaters start ########################################################################################################

          line_moving.add_updater(lambda z: z.become(Line([0,0,0],[np.cos(theta.get_value()*DEGREES),np.sin(theta.get_value()*DEGREES),0],color = PURPLE)))
          a.add_updater(lambda z: z.become(Angle(line_still, line_moving, radius=0.25, other_angle=False)))
          sine.add_updater(lambda z: z.become(Arrow([2*np.cos(theta.get_value()*DEGREES),0,0], [2*np.cos(theta.get_value()*DEGREES),2*np.sin(theta.get_value()*DEGREES),0], buff = 0, color = ORANGE) ))
          cosine.add_updater(lambda z: z.become(Arrow(ORIGIN, [2*np.cos(theta.get_value()*DEGREES),0,0], buff = 0, color = YELLOW)))
 
          sin_theta_symbol.add_updater(lambda z: z.become(z.move_to(sine.get_center() + 0.5*RIGHT)))
          cos_theta_symbol.add_updater(lambda z: z.become(z.move_to(cosine.get_center() + 0.5*DOWN)))

          arrow_moving1.add_updater(lambda z: z.become(Arrow(ORIGIN, [2*np.cos(theta.get_value()*DEGREES),2*np.sin(theta.get_value()*DEGREES),0], buff = 0, color = PURPLE)))
          theta_symbol.add_updater(lambda x: x.move_to(Angle(line_still, line_moving, radius=0.25 + 3 * SMALL_BUFF, other_angle=False).point_from_proportion(0.5)))   

####################### updaters end ########################################################################################################       

         
          
          self.play(AnimationGroup(Create(numberplane,run_time = 4),
                    Create(arrow_moving1, run_time = 2),
                    lag_ratio = 1)
                    )
          self.add(dot)
          self.add(line_still,line_moving,a,theta_symbol,sine,cosine,arrow_moving1,sin_theta_symbol,cos_theta_symbol)
          self.play(theta.animate.set_value(359.999),rate_func = linear,run_time = 6)
          self.play(Uncreate(sin_theta_symbol, run_time = 2),Uncreate(cos_theta_symbol, run_time = 2)) 
          self.remove(sine,cosine,sin_theta_symbol,cos_theta_symbol)
          self.wait()
          
         
          self.play(Transform(arrow_moving1,arrow_moving2,run_time = 3),Uncreate(a,run_time = 3),Uncreate(theta_symbol,run_time = 3))
          self.remove(arrow_moving1,line_still,line_moving,a,theta_symbol)
          self.add(arrow_moving2)
          self.wait()


# added : dot,line_still,line_moving,a,theta_symbol,sine,cosine,arrow_moving1,sin_theta_symbol,cos_theta_symbol,arrow_moving2
# removed : sine,cosine,sin_theta_symbol,cos_theta_symbol,arrow_moving1,line_still,line_moving,a,theta_symbol
# remains : dot,arrow_moving2



######### --------------------------> 2nd stage Begins <------------------------------------#################################




########################### ValueTrackers start #################################################################           
          

          theta = ValueTracker(0.001)



########################### ValueTrackers end ################################################################# 





########################### vectors start ###################################################################################################

        
          sine = Arrow([4*np.cos(theta.get_value()*DEGREES),0,0], [4*np.cos(theta.get_value()*DEGREES),0.5*np.sin(theta.get_value()*DEGREES),0], buff = 0, color = ORANGE) 
          cosine = Arrow(ORIGIN, [4*np.cos(theta.get_value()*DEGREES),0,0], buff = 0, color = YELLOW) 


############################ vectors end ##################################################################################################### 


################### elements necessary for rotation and not displayed on screen start  ############################## 

        

          line_still = Line([0,0,0],[2,0,0])
          line_moving = Line([0,0,0],[np.cos(theta.get_value()*DEGREES),np.sin(theta.get_value()*DEGREES),0],color = PURPLE)



################### elements necessary for rotation and not displayed on screen end ############################## 





############### angles start  #########################


          a = Angle(line_still, line_moving, radius=0.25, other_angle=False)


############### angles end  #########################    



###############################  texts start ##########################################################################

          text = MathTex(r"\theta")
          text.scale(0.6)
          theta_symbol =text.move_to(Angle(line_still, line_moving, radius=0.25 + 3 * SMALL_BUFF, other_angle=False).point_from_proportion(0.5))

         
          text_sine = MathTex(r"2sin(\theta)") 
          text_sine.scale(0.58)
          text_sine.set_color(ORANGE)
          sin_theta_symbol = text_sine.move_to(sine.get_center() + 0.5*RIGHT)

          text_cos = MathTex(r"2cos(\theta)") 
          text_cos.scale(0.58)
          text_cos.set_color(YELLOW)
          cos_theta_symbol = text_cos.move_to(cosine.get_center() + 0.5*DOWN)


###############################  texts end ############################################################################################## 



####################### updaters start ########################################################################################################

          line_moving.add_updater(lambda z: z.become(Line([0,0,0],[np.cos(theta.get_value()*DEGREES),np.sin(theta.get_value()*DEGREES),0],color = PURPLE)))
          a.add_updater(lambda z: z.become(Angle(line_still, line_moving, radius=0.25, other_angle=False)))
          sine.add_updater(lambda z: z.become(Arrow([4*np.cos(theta.get_value()*DEGREES),0,0], [4*np.cos(theta.get_value()*DEGREES),4*np.sin(theta.get_value()*DEGREES),0], buff = 0, color = ORANGE) ))
          cosine.add_updater(lambda z: z.become(Arrow(ORIGIN, [4*np.cos(theta.get_value()*DEGREES),0,0], buff = 0, color = YELLOW)))
 
          sin_theta_symbol.add_updater(lambda z: z.become(z.move_to(sine.get_center() + 0.5*RIGHT)))
          cos_theta_symbol.add_updater(lambda z: z.become(z.move_to(cosine.get_center() + 0.5*DOWN)))

          arrow_moving2.add_updater(lambda z: z.become(Arrow(ORIGIN, [4*np.cos(theta.get_value()*DEGREES),4*np.sin(theta.get_value()*DEGREES),0], buff = 0, color = PURPLE)))
          theta_symbol.add_updater(lambda x: x.move_to(Angle(line_still, line_moving, radius=0.25 + 3 * SMALL_BUFF, other_angle=False).point_from_proportion(0.5)))   

####################### updaters end ########################################################################################################    


          self.remove(arrow_moving2)
          self.add(line_still,line_moving,a,theta_symbol,sine,cosine,sin_theta_symbol,cos_theta_symbol,arrow_moving2)
          self.play(theta.animate.set_value(359.999),rate_func = linear,run_time = 6)
          self.remove(sine,cosine,line_still,line_moving)
          self.play(Transform(arrow_moving2,arrow_moving3,run_time = 3),Uncreate(sin_theta_symbol, run_time = 2),Uncreate(cos_theta_symbol, run_time = 2),Uncreate(theta_symbol, run_time = 2),Uncreate(a, run_time = 2))          
          self.remove(arrow_moving2,sin_theta_symbol,cos_theta_symbol,a,theta_symbol)
          self.add(arrow_moving3)
          self.wait()




######### --------------------------> 3rd stage Begins <------------------------------------#################################



########################### ValueTrackers start #################################################################           
          

          theta = ValueTracker(0.001)



########################### ValueTrackers end ################################################################# 





########################### vectors start ###################################################################################################

        
          sine = Arrow([np.cos(theta.get_value()*DEGREES),0,0], [np.cos(theta.get_value()*DEGREES),np.sin(theta.get_value()*DEGREES),0], buff = 0, color = ORANGE) 
          cosine = Arrow(ORIGIN, [np.cos(theta.get_value()*DEGREES),0,0], buff = 0, color = YELLOW) 


############################ vectors end ##################################################################################################### 


################### elements necessary for rotation and not displayed on screen start  ############################## 

        

          line_still = Line([0,0,0],[0.5,0,0])
          line_moving = Line([0,0,0],[0.5*np.cos(theta.get_value()*DEGREES),0.5*np.sin(theta.get_value()*DEGREES),0],color = PURPLE)



################### elements necessary for rotation and not displayed on screen end ############################## 





############### angles start  #########################


          a = Angle(line_still, line_moving, radius=0.125, other_angle=False)


############### angles end  #########################    



###############################  texts start ##########################################################################

          text = MathTex(r"\theta")
          text.scale(0.35)
          theta_symbol =text.move_to(Angle(line_still, line_moving, radius=0.125 + 3 * SMALL_BUFF, other_angle=False).point_from_proportion(0.5))

         
          text_sine = MathTex(r"\frac{1}{2}sin(\theta)") 
          text_sine.scale(0.35)
          text_sine.set_color(ORANGE)
          sin_theta_symbol = text_sine.move_to(sine.get_center() + 0.5*RIGHT)

          text_cos = MathTex(r"\frac{1}{2}cos(\theta)") 
          text_cos.scale(0.35)
          text_cos.set_color(YELLOW)
          cos_theta_symbol = text_cos.move_to(cosine.get_center() + 0.5*DOWN)


###############################  texts end ############################################################################################## 



####################### updaters start ########################################################################################################

          line_moving.add_updater(lambda z: z.become(Line([0,0,0],[0.5*np.cos(theta.get_value()*DEGREES),0.5*np.sin(theta.get_value()*DEGREES),0],color = PURPLE)))
          a.add_updater(lambda z: z.become(Angle(line_still, line_moving, radius=0.125, other_angle=False)))
          sine.add_updater(lambda z: z.become(Arrow([np.cos(theta.get_value()*DEGREES),0,0], [np.cos(theta.get_value()*DEGREES),np.sin(theta.get_value()*DEGREES),0], buff = 0, color = ORANGE) ))
          cosine.add_updater(lambda z: z.become(Arrow(ORIGIN, [np.cos(theta.get_value()*DEGREES),0,0], buff = 0, color = YELLOW)))
 
          sin_theta_symbol.add_updater(lambda z: z.become(z.move_to(sine.get_center() + 0.5*RIGHT)))
          cos_theta_symbol.add_updater(lambda z: z.become(z.move_to(cosine.get_center() + 0.5*DOWN)))

          arrow_moving3.add_updater(lambda z: z.become(Arrow(ORIGIN, [np.cos(theta.get_value()*DEGREES),np.sin(theta.get_value()*DEGREES),0], buff = 0, color = PURPLE)))
          theta_symbol.add_updater(lambda x: x.move_to(Angle(line_still, line_moving, radius=0.125 + 3 * SMALL_BUFF, other_angle=False).point_from_proportion(0.5)))   

####################### updaters end ########################################################################################################    


          self.remove(arrow_moving3)
          self.add(line_still,line_moving,a,theta_symbol,sine,cosine,sin_theta_symbol,cos_theta_symbol,arrow_moving3)
          self.play(theta.animate.set_value(359.999),rate_func = linear,run_time = 6)
          self.play(Uncreate(sin_theta_symbol, run_time = 2),Uncreate(cos_theta_symbol, run_time = 2),Uncreate(theta_symbol, run_time = 2),Uncreate(a, run_time = 2)) 
          self.remove(sine,cosine,sin_theta_symbol,cos_theta_symbol,a,theta_symbol,line_still,line_moving)
          self.wait()
