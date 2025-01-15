import panel as pn
from alphatims.bruker import TimsTOF
import alphatims.bruker
import alphatims.plotting
import numpy as np
import pandas as pd
import holoviews as hv
from holoviews import streams
import param

hv.extension('bokeh')
pn.extension(sizing_mode="stretch_width")


class DataHandler(param.Parameterized): 
    dataset1 = param.Parameter(default=None) 
    dataset2 = param.Parameter(default=None) 
    bounds_x = param.ClassSelector(class_=streams.BoundsX, default=streams.BoundsX(boundsx=(0, 0)))
    selected_indices = param.Array(default=np.empty(0, dtype=int)) 
    selected_indices2 = param.Array(default=np.empty(0, dtype=int)) 
    # dataframe = param.DataFrame(default=pd.DataFrame()) 

    # frame/RT selection
    frame_slider = pn.widgets.IntRangeSlider(
        show_value=False,
        bar_color='#045082',
        step=1,
        width = 600,
        align = 'center',
        margin=(10, 20, 10, 20)
    )
    frame_start = pn.widgets.IntInput(
        name='Start frame',
        step=1,
        width=100,
        align = 'end',
        styles = {'padding-right' :'10px'},
        
    )
    rt_start = pn.widgets.FloatInput(
        name='Start RT (min)',
        step=0.125,
        width=100,
        format='0,0.000',
        align = 'start',
        styles = {'padding-left' :'10px'},   
    )
    frame_end = pn.widgets.IntInput(
        name='End frame',
        step=1,
        width=100,
        align = 'end',
        styles = {'padding-right' :'10px'},   
    )
    rt_end = pn.widgets.FloatInput(
        name='End RT (min)',
        step=0.125,
        width=100,
        format='0,0.000',
        align = 'start',
        styles = {'padding-left' :'10px'},   
        disabled=False
    )

    # frame/RT selection_2
    frame_slider_2 = pn.widgets.IntRangeSlider(
        show_value=False,
        bar_color='#045082',
        step=1,
        width = 600,
        align = 'center',
        margin=(10, 20, 10, 20)
    )
    frame_start_2 = pn.widgets.IntInput(
        name='Start frame',
        step=1,
        width=100,
        align = 'end',
        styles = {'padding-right' :'10px'},
        
    )
    rt_start_2 = pn.widgets.FloatInput(
        name='Start RT (min)',
        step=0.125,
        width=100,
        format='0,0.000',
        align = 'start',
        styles = {'padding-left' :'10px'},   
    )
    frame_end_2 = pn.widgets.IntInput(
        name='End frame',
        step=1,
        width=100,
        align = 'end',
        styles = {'padding-right' :'10px'},   
    )
    rt_end_2 = pn.widgets.FloatInput(
        name='End RT (min)',
        step=0.125,
        width=100,
        format='0,0.000',
        align = 'start',
        styles = {'padding-left' :'10px'},   
        disabled=False
    )

    # scans/IM selection
    scan_slider = pn.widgets.IntRangeSlider(
        show_value=False,
        bar_color='#045082',
        width = 600,
        align = "center",
        step=1,
        margin=(10, 20, 10, 20)
    )
    scan_start = pn.widgets.IntInput(
        name='Start scan',
        step=1,
        width=100,
        align = 'end',
        styles = {'padding-right' :'10px'},
    )
    im_start = pn.widgets.FloatInput(
        name='Start IM',
        step=0.10,
        width=100,
        align = 'start',
        format='0,0.000',
        styles = {'padding-left' :'10px'},
        disabled=False
    )
    scan_end = pn.widgets.IntInput(
        name='End scan',
        step=1,
        width=100,
        align = 'end',
        styles = {'padding-right' :'10px'},
    )
    im_end = pn.widgets.FloatInput(
        name='End IM',
        step=0.10,
        width=100,
        align = 'start',
        format='0,0.000',
        styles = {'padding-left' :'10px'},
        disabled=False
    )

    # Intensity selection
    intensity_slider = pn.widgets.IntRangeSlider(
        show_value=False,
        bar_color='#045082',
        width = 600,
        align='center',
        step=1,
        margin=(10, 20, 10, 20),
    )
    intensity_start = pn.widgets.IntInput(
        name='Start intensity',
        step=1,
        width=100,
        align='end',
    )
    intensity_end = pn.widgets.IntInput(
        name='End intensity',
        step=1,
        width=100,
        align='start',
    )

    # tof and m/z selection
    tof_slider = pn.widgets.IntRangeSlider(
        show_value=False,
        bar_color='#045082',
        width=600,
        step=1,
        align = 'center',
        margin=(10, 20, 10, 20)
    )
    tof_start = pn.widgets.IntInput(
        name='Start TOF',
        step=1,
        width=100,
        align = 'end',   
         styles = {'padding-right' :'10px'},
    )
    mz_start = pn.widgets.FloatInput(
        name='Start m/z',
        step=0.10,
        width=100,
        format='0.00',
        align = 'start',
        styles = {'padding-left' :'10px'},
        disabled=False
    )
    tof_end = pn.widgets.IntInput(
        name='End TOF',
        step=1,
        width=100,
        align = 'end',
        styles = {'padding-right' :'10px'},
    )
    mz_end = pn.widgets.FloatInput(
        name='End m/z',
        step=0.10,
        width=100,
        format='0.00',
        align = 'start',
        disabled=False,
        styles = {'padding-left' :'10px'},
    )

    # Precursor selection
    select_ms1_precursors = pn.widgets.Checkbox(
        name='Show MS1 ions (precursors)',
        value=True,
        width=200,
        align="center",
        margin=(20, 0, 10, 0)
    )
    select_ms2_fragments = pn.widgets.Checkbox(
        name='Show MS2 ions (fragments)',
        value=False,
        width=200,
        align="center",
    )

    # quad selection
    quad_slider = pn.widgets.RangeSlider(
        show_value=False,
        bar_color='#FF69B4',
        align="center",
        step=1,
        width=600,
        margin=(10, 20, 10, 20),
        disabled=True
    )
    quad_start = pn.widgets.FloatInput(
        name='Start QUAD',
        step=0.50,
        width=100,
        align='end',
        format='0.00',
        disabled=True
    )
    quad_end = pn.widgets.FloatInput(
        name='End QUAD',
        step=0.50,
        width=100,
        format='0.00',
        align='start',
        disabled=True
    )


    #  precursor selection
    precursor_slider = pn.widgets.IntRangeSlider(
        show_value=False,
        bar_color='#FFA500',
        align="center",
        step=1,
        width=600,
        margin=(10, 20, 10, 20),
        disabled=True
    )
    precursor_start = pn.widgets.IntInput(
        name='Start precursor',
        step=1,
        align='end',
        width=120,
        format='0',
        disabled=True
    )
    precursor_end = pn.widgets.IntInput(
        name='End precursor',
        step=1,
        align="start",
        width=120,
        format='0',
        disabled=True
    )

    upload_spinner3 = pn.indicators.LoadingSpinner(
        value=False,
        bgcolor='light',
        color='secondary',
        align = 'end',
        width=30,
        height=30
    )

    #for lineplot
    x_dim_selector_lineplot = pn.widgets.Select(name='X-axis Dimension', options=['mz', 'rt', 'mobility'], value='rt',styles={"font-size":"20px"})
    y_dim_selector_lineplot = pn.widgets.Select(name='Y-axis Dimension', options=['intensity','mz', 'rt', 'mobility'], value='intensity',styles={"font-size":"20px"})

    #for heatmap
    x_dim_selector_heatmap = pn.widgets.Select(name='X-axis Dimension', options=['mz', 'rt', 'mobility'], value='mz',styles={"font-size":"20px"})
    y_dim_selector_heatmap = pn.widgets.Select(name='Y-axis Dimension', options=['mz', 'rt', 'mobility'], value='mobility',styles={"font-size":"20px"})
    z_dim_selector_heatmap = pn.widgets.Select(name='Z-axis Dimension', options=['intensity','mz', 'rt', 'mobility'], value='intensity',styles={"font-size":"20px"})

    max_frame_index = 0
    max_rt_value = 0
    max_scan = 0
    max_im = 0
    max_intensity = 0
    max_tof = 0
    max_mz = 0
    max_quad = min_quad = 0
    max_precursor = min_precursor = 1

    @param.depends('dataset1', 'dataset2', watch=True) 
    def update_slider_limits(self): 
        # Determine the maximum frame index and RT value based on available datasets 
        if self.dataset1 and self.dataset2: 
            self.max_frame_index = max(self.dataset1.frame_max_index, self.dataset2.frame_max_index) 
            self.max_rt_value = max(self.dataset1.rt_max_value, self.dataset2.rt_max_value) / 60 

            self.max_scan = max(self.dataset1.scan_max_index,self.dataset2.scan_max_index)
            self.max_im = max(self.dataset1.mobility_max_value,self.dataset2.mobility_max_value)

            self.max_intensity = int(max(self.dataset1.intensity_max_value,self.dataset2.intensity_max_value))+1

            self.max_tof = max(self.dataset1.tof_max_index,self.dataset2.tof_max_index)
            self.max_mz = max(self.dataset1.mz_max_value,self.dataset2.mz_max_value)

            self.max_quad = max(self.dataset1.quad_mz_max_value,self.dataset2.quad_mz_max_value)
            self.min_quad = min(self.dataset1.quad_mz_min_value,self.dataset2.quad_mz_min_value)
            self.max_precursor = max(self.dataset1.precursor_max_index,self.dataset2.precursor_max_index)

        elif self.dataset1: 
            self.max_frame_index = self.dataset1.frame_max_index 
            self.max_rt_value = self.dataset1.rt_max_value / 60 

            self.max_scan = self.dataset1.scan_max_index
            self.max_im = self.dataset1.mobility_max_value

            self.max_intensity = self.dataset1.intensity_max_value

            self.max_tof = self.dataset1.tof_max_index
            self.max_mz = self.dataset1.mz_max_value

            self.max_quad = self.dataset1.quad_mz_max_value
            self.min_quad = self.dataset1.quad_mz_min_value
            self.max_precursor = self.dataset1.precursor_max_index


        elif self.dataset2: 
            self.max_frame_index = self.dataset2.frame_max_index 
            self.max_rt_value = self.dataset2.rt_max_value / 60

            self.max_scan = self.dataset2.scan_max_index
            self.max_im = self.dataset2.mobility_max_value

            self.max_intensity = self.dataset2.intensity_max_value

            self.max_tof = self.dataset2.tof_max_index
            self.max_mz = self.dataset2.mz_max_value

            self.max_quad = self.dataset2.quad_mz_max_value
            self.min_quad = self.dataset2.quad_mz_min_value
            self.max_precursor = self.dataset2.precursor_max_index

        # frame, rt values range setup initially
        self.frame_slider.start,self.frame_slider_2.start = 0,0
        self.frame_slider.end,self.frame_slider_2.end = self.max_frame_index, self.max_frame_index
        self.frame_slider.value, self.frame_slider_2.value = (0, self.max_frame_index), (0, self.max_frame_index)

        self.frame_start.start, self.frame_start_2.start = 0,0
        self.frame_start.end, self.frame_start_2.end = self.max_frame_index, self.max_frame_index 
        self.frame_start.value, self.frame_start_2.value = 0,0

        self.frame_end.start, self.frame_end_2.start = 0, 0
        self.frame_end.end, self.frame_end_2.end = self.max_frame_index, self.max_frame_index 
        self.frame_end.value, self.frame_end_2.value = self.max_frame_index, self.max_frame_index

        self.rt_start.start, self.rt_start_2.start = 0, 0
        self.rt_start.end, self.rt_start_2.end = self.max_rt_value, self.max_rt_value
        self.rt_start.value, self.rt_start_2.value = 0, 0

        self.rt_end.start, self.rt_end_2.start = 0, 0
        self.rt_end.end, self.rt_end_2.end = self.max_rt_value, self.max_rt_value
        self.rt_end.value, self.rt_end_2.value = self.max_rt_value, self.max_rt_value


        # scan, im values range setup initially
        self.scan_slider.start, self.scan_slider.end = (0,self.max_scan)
        self.scan_slider.value = (0,self.max_scan)

        self.scan_start.start, self.scan_start.end = (0,self.max_scan)
        self.scan_start.value = 0

        self.scan_end.start, self.scan_end.end = (0,self.max_scan)
        self.scan_end.value = self.max_scan

        self.im_start.start, self.im_start.end = (0, self.max_im)
        self.im_start.value = 0

        self.im_end.start, self.im_end.end = (0, self.max_im) 
        self.im_end.value = self.max_im

        # intensity values range setup initially
        self.intensity_slider.start,  self.intensity_slider.end = (0,self.max_intensity)
        self.intensity_slider.value = (0,self.max_intensity)

        self.intensity_start.start,  self.intensity_start.end = (0,self.max_intensity)
        self.intensity_start.value = 0

        self.intensity_end.start,  self.intensity_end.end = (0,self.max_intensity)
        self.intensity_end.value = self.max_intensity

        # tof/mz values range setup initially

        self.tof_slider.start, self.tof_slider.end = (0,self.max_tof)
        self.tof_slider.value = (0,self.max_tof)

        self.tof_start.start, self.tof_start.end = (0,self.max_tof)
        self.tof_start.value = 0

        self.tof_end.start, self.tof_end.end = (0,self.max_tof)
        self.tof_end.value = self.max_tof

        self.mz_start.start, self.mz_start.end = (0, self.max_mz)
        self.mz_start.value = 0

        self.mz_end.start, self.mz_end.end = (0, self.max_mz) 
        self.mz_end.value = self.max_mz

        # quad/ precusor values range setup initially

        if self.dataset1.acquisition_mode == "diaPASEF":
            self.precursor_start.name = "Start window group"
            self.precursor_end.name = "End window group"
        else:
            self.precursor_start.name = "Start precursor"
            self.precursor_end.name = "End precursor"
        
        self.select_ms1_precursors.value = True
        if self.select_ms2_fragments.value:
            self.select_ms2_fragments.value = False
            #self.update_toggle_fragments()
            self.quad_slider.disabled = True
            self.quad_start.disabled = True
            self.quad_end.disabled = True
            self.precursor_slider.disabled = True
            self.precursor_start.disabled = True
            self.precursor_end.disabled = True

        self.quad_slider.start, self.quad_slider.end = (self.min_quad, self.max_quad)
        self.quad_slider.value = (self.min_quad, self.max_quad)
        self.quad_start.start, self.quad_start.end = (self.min_quad, self.max_quad)
        self.quad_end.start, self.quad_end.end = (self.min_quad, self.max_quad)
        self.quad_start.value, self.quad_end.value= (self.min_quad, self.max_quad)

        self.precursor_slider.start, self.precursor_slider.end = (self.min_precursor, self.max_precursor)
        self.precursor_slider.value = (self.min_precursor, self.max_precursor)
        self.precursor_start.start, self.precursor_start.end = (self.min_precursor, self.max_precursor)
        self.precursor_end.start, self.precursor_end.end = (self.min_precursor, self.max_precursor)
        self.precursor_start.value, self.precursor_end.value = (self.min_precursor, self.max_precursor)


        self.setup_callbacks()
        self.update_bounds(self.rt_start.value,self.rt_end.value)

    def sync_values_from_slider(self, event): 
        start, end = event.new 
        self.frame_start.value = start 
        self.frame_end.value = end 
         
        self.rt_start.value = start * self.max_rt_value / self.max_frame_index 
        self.rt_end.value = end * self.max_rt_value / self.max_frame_index 
        self.update_bounds(self.rt_start.value,self.rt_end.value)
        
    def sync_slider_from_values(self, event): 
        self.frame_slider.value = (self.frame_start.value, self.frame_end.value) 
    
    def sync_rt_from_frame_start(self, event): 
        self.rt_start.value = event.new * self.max_rt_value / self.max_frame_index 
        
    def sync_rt_from_frame_end(self, event): 
        self.rt_end.value = event.new * self.max_rt_value / self.max_frame_index

    def sync_frame_from_rt_start(self, event):  
        self.frame_start.value = int(event.new * self.max_frame_index / self.max_rt_value)

    def sync_frame_from_rt_end(self, event): 
        self.frame_end.value = int(event.new * self.max_frame_index / self.max_rt_value)

    # --------------------------------------------------------------------------------------------------------
    # frame slider 2

    def sync_values_from_frame_slider_2(self, event): 
        start, end = event.new 
        print("event2: ",event)
        self.frame_start_2.value = start 
        self.frame_end_2.value = end 
         
        self.rt_start_2.value = start * self.max_rt_value / self.max_frame_index 
        self.rt_end_2.value = end * self.max_rt_value / self.max_frame_index 
        
        
    def sync_frame_slider_2_from_values(self, event): 
        self.frame_slider_2.value = (self.frame_start_2.value, self.frame_end_2.value) 
    
    def sync_rt_from_frame_start_2(self, event): 
        self.rt_start_2.value = event.new * self.max_rt_value / self.max_frame_index 
        
    def sync_rt_from_frame_end_2(self, event): 
        self.rt_end_2.value = event.new * self.max_rt_value / self.max_frame_index

    def sync_frame_from_rt_start_2(self, event):  
        self.frame_start_2.value = int(event.new * self.max_frame_index / self.max_rt_value)

    def sync_frame_from_rt_end_2(self, event): 
        self.frame_end_2.value = int(event.new * self.max_frame_index / self.max_rt_value)
    
    #----------------------------------------------------------------------------------------------------------
    # scan slider

    def sync_values_from_scan_slider(self, event): 
        start, end = event.new 
        self.scan_start.value = start 
        self.scan_end.value = end 
         
        self.im_start.value = start * self.max_im / self.max_scan
        self.im_end.value = end * self.max_im / self.max_scan
        
    def sync_scan_slider_from_values(self, event): 
        self.scan_slider.value = (self.scan_start.value, self.scan_end.value) 
    
    def sync_im_from_scan_start(self, event): 
        self.im_start.value = event.new * self.max_im / self.max_scan
        
    def sync_im_from_scan_end(self, event): 
        self.im_end.value = event.new * self.max_im / self.max_scan

    def sync_scan_from_im_start(self, event):  
        self.scan_start.value = int(event.new * self.max_scan / self.max_im)

    def sync_scan_from_im_end(self, event): 
        self.scan_end.value = int(event.new * self.max_scan / self.max_im)

    #----------------------------------------------------------------------------------------------------------
    # intensities

    def sync_values_from_intensity_slider(self, event): 
        start, end = event.new 
        self.intensity_start.value = start 
        self.intensity_end.value = end 
        
        
    def sync_intensity_slider_from_values(self, event): 
        self.intensity_slider.value = (self.intensity_start.value, self.intensity_end.value) 

    #----------------------------------------------------------------------------------------------------------
    # tof/ mz

    def sync_values_from_tof_slider(self, event): 
        start, end = event.new 
        self.tof_start.value = start 
        self.tof_end.value = end 
         
        self.mz_start.value = start * self.max_mz / self.max_tof
        self.mz_end.value = end * self.max_mz / self.max_tof
       
        
    def sync_tof_slider_from_values(self, event): 
        self.tof_slider.value = (self.tof_start.value, self.tof_end.value) 
    
    def sync_mz_from_tof_start(self, event): 
        self.mz_start.value = event.new * self.max_mz / self.max_tof
        
    def sync_mz_from_tof_end(self, event): 
        self.im_end.value = event.new * self.max_mz / self.max_tof

    def sync_tof_from_mz_start(self, event):  
        self.tof_start.value = int(event.new * self.max_tof / self.max_mz)

    def sync_tof_from_mz_end(self, event): 
        self.tof_end.value = int(event.new * self.max_tof / self.max_mz)
    
    #----------------------------------------------------------------------------------------------------------
    # quad slider

    def sync_values_from_quad_slider(self, event): 
        start, end = event.new 
        self.quad_start.value = start 
        self.quad_end.value = end 
        
    def sync_quad_slider_from_values(self, event): 
        self.quad_slider.value = (self.quad_start.value, self.quad_end.value)
    
    #----------------------------------------------------------------------------------------------------------
    # precursor slider

    def sync_values_from_precursor_slider(self, event): 
        start, end = event.new 
        self.precursor_start.value = start 
        self.precursor_end.value = end 
        
    def sync_precursor_slider_from_values(self, event): 
        self.precursor_slider.value = (self.precursor_start.value, self.precursor_end.value)
    #----------------------------------------------------------------------------------------------------------

    def sync_plot_from_ms2(self, event=None):
        self.update_toggle_fragments()
        print("update_toggle_fragments: ",event.new)
        return
    
    def plotting_graphs(self,event=None):
        self.upload_spinner3.value = True
        self.selected_indices = self.setup_indices()
        self.selected_indices2 = self.setup_indices2()
        self.upload_spinner3.value = False
    
    def setup_callbacks2(self):
    # Bind the checkboxes to the functions
        self.select_ms2_fragments.param.watch(self.sync_plot_from_ms2, "value")

    def setup_callbacks(self): 
        self.frame_slider.param.watch(self.sync_values_from_slider, 'value')
        self.frame_start.param.watch(self.sync_slider_from_values, 'value') 
        self.frame_end.param.watch(self.sync_slider_from_values, 'value') 
        self.frame_start.param.watch(self.sync_rt_from_frame_start, 'value') 
        self.frame_end.param.watch(self.sync_rt_from_frame_end, 'value')
        self.rt_start.param.watch(self.sync_frame_from_rt_start, 'value') 
        self.rt_end.param.watch(self.sync_frame_from_rt_end, 'value')

        self.frame_slider_2.param.watch(self.sync_values_from_frame_slider_2, 'value')
        self.frame_start_2.param.watch(self.sync_frame_slider_2_from_values, 'value') 
        self.frame_end_2.param.watch(self.sync_frame_slider_2_from_values, 'value') 
        self.frame_start_2.param.watch(self.sync_rt_from_frame_start_2, 'value') 
        self.frame_end_2.param.watch(self.sync_rt_from_frame_end_2, 'value')
        self.rt_start_2.param.watch(self.sync_frame_from_rt_start_2, 'value') 
        self.rt_end_2.param.watch(self.sync_frame_from_rt_end_2, 'value')

        self.scan_slider.param.watch(self.sync_values_from_scan_slider, 'value')
        self.scan_start.param.watch(self.sync_scan_slider_from_values, 'value') 
        self.scan_end.param.watch(self.sync_scan_slider_from_values, 'value') 
        self.scan_start.param.watch(self.sync_im_from_scan_start, 'value') 
        self.scan_end.param.watch(self.sync_im_from_scan_end, 'value')
        self.im_start.param.watch(self.sync_scan_from_im_start, 'value') 
        self.im_end.param.watch(self.sync_scan_from_im_end, 'value')

        self.intensity_slider.param.watch(self.sync_values_from_intensity_slider, 'value')
        self.intensity_start.param.watch(self.sync_intensity_slider_from_values, 'value') 
        self.intensity_end.param.watch(self.sync_intensity_slider_from_values, 'value') 

        self.tof_slider.param.watch(self.sync_values_from_tof_slider, 'value')
        self.tof_start.param.watch(self.sync_tof_slider_from_values, 'value') 
        self.tof_end.param.watch(self.sync_tof_slider_from_values, 'value') 
        self.tof_start.param.watch(self.sync_mz_from_tof_start, 'value') 
        self.tof_end.param.watch(self.sync_mz_from_tof_end, 'value')
        self.mz_start.param.watch(self.sync_tof_from_mz_start, 'value') 
        self.mz_end.param.watch(self.sync_tof_from_mz_end, 'value')

        self.quad_slider.param.watch(self.sync_values_from_quad_slider, 'value')
        self.quad_start.param.watch(self.sync_quad_slider_from_values, 'value') 
        self.quad_end.param.watch(self.sync_quad_slider_from_values, 'value')

        self.precursor_slider.param.watch(self.sync_values_from_precursor_slider, 'value')
        self.precursor_start.param.watch(self.sync_precursor_slider_from_values, 'value') 
        self.precursor_end.param.watch(self.sync_precursor_slider_from_values, 'value')
        
    
    def update_toggle_fragments(self):
        self.quad_slider.disabled = not self.quad_slider.disabled
        self.quad_start.disabled = not self.quad_start.disabled
        self.quad_end.disabled = not self.quad_end.disabled
        self.precursor_slider.disabled = not self.precursor_slider.disabled
        self.precursor_start.disabled = not self.precursor_start.disabled
        self.precursor_end.disabled = not self.precursor_end.disabled

    # Function to create the range highlight
    def highlight_range(self,boundsx):
        return hv.VSpan(boundsx[0], boundsx[1]).opts(color='orange', alpha=0.3)

    # Callback to update the BoundsX stream when the slider changes
    def update_bounds(self,rt_start,rt_end):
        print("lahiru: ",rt_start,rt_end)
        self.bounds_x.event(boundsx=(rt_start, rt_end))

    def update_plot_tic_1(self): 
        """ Updates the TIC plot based on the dataset1. 
        
        Returns: A HoloViews plot object or a Markdown pane. 
        """ 
        if self.dataset1 is not None: 
            tic = alphatims.plotting.tic_plot(self.dataset1, title=self.dataset1.sample_name, width=900)
            #self.update_bounds(self.rt_start.value,self.rt_end.value)
            # DynamicMap to create the highlight overlay
            dmap = hv.DynamicMap(self.highlight_range, streams=[self.bounds_x])
            fig = tic * dmap
            return fig
        
            
        else: return pn.pane.Markdown("**Please upload first dataset.**") 

    @pn.depends('dataset1', watch=True) 
    def update_selected_indices_1(self):
        self.selected_indices = self.setup_indices()
    
    @pn.depends('dataset2', watch=True) 
    def update_selected_indices_2(self):
        self.selected_indices2 = self.setup_indices2()

    @pn.depends('dataset1') 
    def update_plots_1(self):
        self.update_plot_tic_1() 

    @pn.depends('dataset2') 
    def update_plots_2(self): 
        self.update_plot_tic_2()
        
    def update_plot_tic_2(self): 
        """ Updates the TIC plot based on the dataset1. 
        
        Returns: A HoloViews plot object or a Markdown pane. 
        """ 
        if self.dataset2 is not None: 
            tic = alphatims.plotting.tic_plot(self.dataset2, title=self.dataset2.sample_name, width=900)
            #self.update_bounds(self.rt_start.value,self.rt_end.value)
            # DynamicMap to create the highlight overlay
            dmap = hv.DynamicMap(self.highlight_range, streams=[self.bounds_x])
            fig = tic * dmap
            return fig 
        else: return pn.pane.Markdown("**Please upload second dataset.**") 
        
    def upload_callback_1(self, event=None): 
        file_path1 = upload_file1.value
        print("file_path1: ",file_path1)
       
        if file_path1: 
            print("file1 uploading...") 
            upload_spinner1.value = True 
            try: 
                # Process the file from the provided file path 
                self.dataset1 = TimsTOF(file_path1) 
                if self.dataset1: 
                    print("Dataset1 Loaded")
                upload_spinner1.value = False 
                upload_error.object = ""
                file_path1 = "" 
            except Exception as e: 
                upload_spinner1.value = False 
                upload_error.object = f"Error processing file: {e}" 
            finally: upload_spinner1.value = False

    def upload_callback_2(self, event=None): 
        file_path2 = upload_file2.value
        print("file_path2: ",file_path2)

        if file_path2: 
            print("file2 uploading ...") 
            upload_spinner2.value = True 
            try: 
                # Process the file from the provided file path 
                self.dataset2 = TimsTOF(file_path2) 
                if self.dataset2: 
                    print("Dataset2 Loaded") 
                upload_spinner2.value = False 
                upload_error.object = "" 
                file_path2 =""
            except Exception as e: 
                upload_spinner2.value = False 
                upload_error.object = f"Error processing file: {e}" 
            finally: upload_spinner2.value = False
    
    def setup_indices(self):
        if self.dataset1:
            frame_indices = alphatims.bruker.convert_slice_key_to_int_array(self.dataset1, slice(*self.frame_slider_2.value), "frame_indices")
            scan_indices = alphatims.bruker.convert_slice_key_to_int_array(self.dataset1, slice(*self.scan_slider.value), "scan_indices")
            if self.select_ms1_precursors.value:
                quad_values = np.array([[-1, 0]])
                precursor_indices = np.array([[0, 1, 1]])
            else:
                quad_values = np.empty(shape=(0, 2), dtype=np.float64)
                precursor_indices = np.empty(shape=(0, 3), dtype=np.int64)
            if self.select_ms2_fragments.value:
                quad_values_ = alphatims.bruker.convert_slice_key_to_float_array(
                        slice(*self.quad_slider.value)
                    )
                precursor_indices_ = alphatims.bruker.convert_slice_key_to_int_array(
                        self.dataset1, slice(*self.precursor_slider.value), "precursor_indices"
                    )
                quad_values = np.vstack([quad_values, quad_values_])
                precursor_indices = np.vstack([precursor_indices, precursor_indices_])
            tof_indices = alphatims.bruker.convert_slice_key_to_int_array(
                        self.dataset1, slice(*self.tof_slider.value), "tof_indices"
                    )
            intensity_values = alphatims.bruker.convert_slice_key_to_float_array(
                        slice(*self.intensity_slider.value)
                    )
            print("frame_indices1",frame_indices)
            print("scan_slices1",scan_indices)
            print("intensity_values1",intensity_values)
            print("tof_indices1", tof_indices)

            selected_indices = alphatims.bruker.filter_indices(
                        frame_slices=frame_indices,
                        scan_slices=scan_indices,
                        precursor_slices=precursor_indices,
                        tof_slices=tof_indices,
                        quad_slices=quad_values,
                        intensity_slices=intensity_values,
                        frame_max_index=self.dataset1.frame_max_index,
                        scan_max_index=self.dataset1.scan_max_index,
                        push_indptr=self.dataset1.push_indptr,
                        precursor_indices=self.dataset1.precursor_indices,
                        quad_mz_values=self.dataset1.quad_mz_values,
                        quad_indptr=self.dataset1.quad_indptr,
                        tof_indices=self.dataset1.tof_indices,
                        intensities=self.dataset1.intensity_values
                    )
            # self.dsd(selected_indices)
            return selected_indices
    

    def setup_indices2(self):
        if self.dataset2:
            frame_indices = alphatims.bruker.convert_slice_key_to_int_array(self.dataset2, slice(*self.frame_slider_2.value), "frame_indices")
            scan_indices = alphatims.bruker.convert_slice_key_to_int_array(self.dataset2, slice(*self.scan_slider.value), "scan_indices")
            if self.select_ms1_precursors.value:
                quad_values = np.array([[-1, 0]])
                precursor_indices = np.array([[0, 1, 1]])
            else:
                quad_values = np.empty(shape=(0, 2), dtype=np.float64)
                precursor_indices = np.empty(shape=(0, 3), dtype=np.int64)
            if self.select_ms2_fragments.value:
                quad_values_ = alphatims.bruker.convert_slice_key_to_float_array(
                        slice(*self.quad_slider.value)
                    )
                precursor_indices_ = alphatims.bruker.convert_slice_key_to_int_array(
                        self.dataset2, slice(*self.precursor_slider.value), "precursor_indices"
                    )
                quad_values = np.vstack([quad_values, quad_values_])
                precursor_indices = np.vstack([precursor_indices, precursor_indices_])
            tof_indices = alphatims.bruker.convert_slice_key_to_int_array(
                        self.dataset2, slice(*self.tof_slider.value), "tof_indices"
                    )
            intensity_values = alphatims.bruker.convert_slice_key_to_float_array(
                        slice(*self.intensity_slider.value)
                    )
            print("frame_indices2",frame_indices)
            print("scan_slices2",scan_indices)
            print("intensity_values2",intensity_values)
            print("tof_indices2", tof_indices)

            selected_indices = alphatims.bruker.filter_indices(
                        frame_slices=frame_indices,
                        scan_slices=scan_indices,
                        precursor_slices=precursor_indices,
                        tof_slices=tof_indices,
                        quad_slices=quad_values,
                        intensity_slices=intensity_values,
                        frame_max_index=self.dataset2.frame_max_index,
                        scan_max_index=self.dataset2.scan_max_index,
                        push_indptr=self.dataset2.push_indptr,
                        precursor_indices=self.dataset2.precursor_indices,
                        quad_mz_values=self.dataset2.quad_mz_values,
                        quad_indptr=self.dataset2.quad_indptr,
                        tof_indices=self.dataset2.tof_indices,
                        intensities=self.dataset2.intensity_values
                    )
            
            return selected_indices
        else:
            return np.array([])

    # def dsd(self,selected_indices):
    #     chunk_size = 100000  # Adjust based on your system's capacity
    #     chunks = [selected_indices[i:i + chunk_size] for i in range(0, len(selected_indices), chunk_size)]

    #     dfs = []
    #     for chunk in chunks:
    #         df_chunk = self.dataset1.as_dataframe(chunk)
    #         dfs.append(df_chunk)

    #     df = pd.concat(dfs, ignore_index=True)
    #     print("dataframe length: ",len(df))

    # line_plot functions
    def plot_lineplot(self,x_dim,y_dim,selected_indices):
        if self.dataset1 is not None:  # Ensure dataset is loaded
            # Validate selected dimensions
            valid_x_dims = ['mz', 'rt', 'mobility']
            valid_y_dims = ['intensity', 'mz', 'rt', 'mobility']
            if x_dim in valid_x_dims and y_dim in valid_y_dims: 
                # Create the plot
                plot = alphatims.plotting.line_plot(
                    self.dataset1,
                    selected_indices,
                    x_dim,
                    self.dataset1.sample_name,
                    y_dim
                )
                print("acquisition_mode1: ",self.dataset1.acquisition_mode)
                return plot  # Dynamically update the plot
            else:
                return pn.pane.Markdown("**Invalid dimensions selected.**")
        else:
            return pn.pane.Markdown("**First dataset is not loaded.**")
    
    # line_plot functions
    def plot_lineplot2(self,x_dim,y_dim,selected_indices):
        if self.dataset2 is not None:  # Ensure dataset is loaded
            # Validate selected dimensions
            valid_x_dims = ['mz', 'rt', 'mobility']
            valid_y_dims = ['intensity', 'mz', 'rt', 'mobility']
            if x_dim in valid_x_dims and y_dim in valid_y_dims: 
                # Create the plot
                plot = alphatims.plotting.line_plot(
                    self.dataset2,
                    selected_indices,
                    x_dim,
                    self.dataset2.sample_name,
                    y_dim
                )
                print("acquisition_mode2: ",self.dataset1.acquisition_mode)
                return plot  # Dynamically update the plot
            else:
                return pn.pane.Markdown("**Invalid dimensions selected.**")
        else:
            return pn.pane.Markdown("**Second dataset is not loaded.**")
    
    # line_plot functions
    # def plot_heatmap(self,x_dim,y_dim,z_dim,dataframe):
    #     if self.dataset1 is not None:  # Ensure dataset is loaded
    #         # Validate selected dimensions
    #         valid_x_dims = ['mz', 'rt', 'mobility']
    #         valid_y_dims = ['mz', 'rt', 'mobility']
    #         valid_z_dims = ['intensity', 'mz', 'rt', 'mobility']
    #         if x_dim in valid_x_dims and y_dim in valid_y_dims and z_dim in valid_z_dims: 
    #             print("x_dim",x_dim)
    #             print("y_dim",y_dim)
    #             print("z_dim",z_dim)
                                               
    #             print("dataframe: ",dataframe)
    #             # Create the plot
    #             plot = alphatims.plotting.heatmap(
    #                 dataframe,
    #                 x_dim,
    #                 y_dim,
    #                 self.dataset1.sample_name,
    #                 z_dim,
    #             )
    #             print("test 10")
    #             print("acquisition_mode: ",self.dataset1.acquisition_mode)
    #             return plot  # Dynamically update the plot
    #         else:
    #             return pn.pane.Markdown("Invalid dimensions selected.")
    #     else:
    #         return pn.pane.Markdown("Dataset is not loaded.")




data_handler = DataHandler()
data_handler.setup_callbacks2()

divider_descr = pn.pane.HTML(
    '<hr style="height: 6px; border:none; background-color: #045082">',
    sizing_mode='stretch_width',
    align='center'
)

instruction1 = pn.pane.Markdown("### Please upload 1<sup>st</sup> experimental .hdf file below:", 
                                sizing_mode='stretch_width',
                                margin=(0, 0, 0, 0) )

instruction2 = pn.pane.Markdown("### Please upload 2<sup>nd</sup> experimental .hdf file below:", 
                                sizing_mode='stretch_width',
                                margin=(0, 0, 0, 0) )

upload_file1 = pn.widgets.TextInput(
        placeholder='Enter the whole path to .hdf file',
        align="center",
        width=10,
        sizing_mode="stretch_width",
    )

upload_file2 = pn.widgets.TextInput(
        placeholder='Enter the whole path to .hdf file',
        align="center",
        width=10,
        sizing_mode="stretch_width",
    )

plot_button = pn.widgets.Button(
    name='Plot',
    button_type='primary',
    height=30,
    width=100,
)

upload_button1 = pn.widgets.Button(
    name='Upload Data',
    button_type='primary',
    height=30,
    width=100,
)

upload_button2 = pn.widgets.Button(
    name='Upload Data',
    button_type='primary',
    height=30,
    width=100,
)

upload_spinner1 = pn.indicators.LoadingSpinner(
    value=False,
    bgcolor='light',
    color='secondary',
    align = 'end',
    width=40,
    height=40
)

upload_spinner2 = pn.indicators.LoadingSpinner(
    value=False,
    bgcolor='light',
    color='secondary',
    align = 'end',
    width=40,
    height=40
)

upload_error = pn.pane.Alert(
    # width=800,
    sizing_mode="stretch_width",
    alert_type="danger",
    align='center',
    margin=(-15, 0, -5, 0),
)



# SAVE SLICED DATA
save_sliced_data_path = pn.widgets.TextInput(
    name='Specify a path to save the currently selected data as .csv file:',
    placeholder='e.g. D:\Bruker',
    margin=(15, 10, 0, 10)
)
save_sliced_data_overwrite = pn.widgets.Checkbox(
    name='overwrite',
    value=False,
    width=80,
)
save_sliced_data_button = pn.widgets.Button(
    name='Save as CSV',
    button_type='primary',
    height=31,
    width=100,
)
save_sliced_data_spinner = pn.indicators.LoadingSpinner(
    value=False,
    bgcolor='light',
    color='secondary',
    width=30,
    height=30
)
save_sliced_data_message = pn.pane.Alert(
    alert_type='success',
    margin=(-15, 5, -10, 15),
    width=50
)



project_description = pn.pane.Markdown("**Fast Accession** and **Visualization** of unprocessed **LC-TIMS-Q-TOF data** from Bruker’s timsTOF Pro instruments.",styles={"font_size":"25px",'text-align':'center'})

def show_widget_box1(dataset1, dataset2): 
    if dataset1 or dataset2: 
        return pn.WidgetBox(
                    pn.pane.Markdown('## Total Ion Chromatogram (TIC) Plots',),
                    pn.Column(
                        data_handler.frame_slider,
                        pn.Row(
                            pn.WidgetBox(
                                data_handler.frame_start,
                            ),
                            pn.WidgetBox(
                                data_handler.rt_start,
                            ),
                            pn.WidgetBox(
                                data_handler.frame_end,
                            ),
                            pn.WidgetBox(
                                data_handler.rt_end,
                            ),
                            width=600,
                            align = 'center',
                            styles={'padding': '20px'},   
                        ),
                    ),
                    
                    pn.Row( 
                        pn.WidgetBox( 
                            data_handler.update_plot_tic_1,  
                        ), 
                        pn.WidgetBox( 
                            data_handler.update_plot_tic_2,  
                        ), 
                            styles={"padding-bottom": "10px"},
                    ),  
                    styles={'border': '1px solid #ccc', 'padding': '10px'},       
                )             
    return None                

def show_widget_box2(dataset1, dataset2):
    if dataset1 or dataset2:  
        return pn.WidgetBox(
                    pn.pane.Markdown('# Advanced Visualization',),        
                    pn.Column(
                            pn.WidgetBox(
                                pn.pane.Markdown('## Parameters',),
                                pn.Row(
                                    pn.Column(
                                        pn.Card(
                                            data_handler.select_ms1_precursors,
                                            data_handler.select_ms2_fragments,
                                            
                                             pn.WidgetBox(
                                                data_handler.quad_slider,
                                                pn.Row(
                                                    pn.WidgetBox(
                                                        data_handler.quad_start,
                                                    ),
                                                    pn.WidgetBox(
                                                        data_handler.quad_end,
                                                    ),     
                                                    
                                                ),
                                            styles = {"padding-bottom":"20px"},
                                            ),
                                            
                                            pn.WidgetBox(
                                                data_handler.precursor_slider,
                                                pn.Row(
                                                    pn.WidgetBox(
                                                        data_handler.precursor_start,
                                                    ),
                                                    pn.WidgetBox(
                                                        data_handler.precursor_end,
                                                    ),
                                                ),
                                                styles = {"padding-bottom":"20px"},
                                            ),
                                            
                                            title='Select Quad Values/ Precusor Indices (QUADRUPOLE)',
                                            collapsed=False,
                                            styles = {"padding":"20px"},
                                            height = 400,
                                        ),

                                        pn.Card(
                                            data_handler.tof_slider,
                                            pn.Row(
                                                pn.WidgetBox(
                                                    data_handler.tof_start,
                                                ),
                                                pn.WidgetBox(
                                                    data_handler.mz_start,
                                                ),
                                                pn.WidgetBox(
                                                    data_handler.tof_end,
                                                ),
                                                pn.WidgetBox(
                                                    data_handler.mz_end,
                                                ),   
                                            ),
                                            title='Select MZ Values (TOF)',
                                            styles = {"padding":"20px"},
                                            collapsed=False,
                                            height = 200,
                                        ),
                                        styles = {"padding":"10px"},

                                    ),
                                    pn.Column(
                                        pn.Card(
                                            data_handler.frame_slider_2,
                                            pn.Row(
                                               pn.WidgetBox(
                                                        data_handler.frame_start_2,
                                                    ),
                                                pn.WidgetBox(
                                                         data_handler.rt_start_2,
                                                    ),    
                                                   
                                                pn.WidgetBox(
                                                    data_handler.frame_end_2,
                                                ),
                                                pn.WidgetBox(
                                                    data_handler.rt_end_2,
                                                ),         
                                                
                                            ),
                                            title='Select Retention Time Values/ Frame Indices (LC)',
                                            styles = {"padding":"20px"},
                                            collapsed=False,
                                            height = 200,
                                        ),

                                        pn.Card(
                                            data_handler.scan_slider,
                                            pn.Row(
                                                pn.WidgetBox(
                                                    data_handler.scan_start,
                                                ),
                                                pn.WidgetBox(
                                                    data_handler.im_start,
                                                ),  
                                                
                                                pn.WidgetBox(
                                                    data_handler.scan_end,
                                                ),
                                                pn.WidgetBox(
                                                    data_handler.im_end,
                                                ),   
                                            ),
                                            title='Select Mobility Values/ Scan Indices (TIMS)',
                                            styles = {"padding":"20px"},
                                            collapsed=False,
                                            height = 200,
                                        ),

                                        pn.Card(
                                            data_handler.intensity_slider,
                                            pn.Row(
                                                pn.WidgetBox(
                                                    data_handler.intensity_start,
                                                ),
                                                pn.WidgetBox(
                                                    data_handler.intensity_end,
                                                ),                         
                                            ),
                                            title='Select Intensity Values (DETECTOR)',
                                            styles = {"padding":"20px"},
                                            collapsed=False,
                                            height = 200,
                                        ),
                                        styles = {"padding":"10px"},
                                    ),
                                ),
                                pn.WidgetBox(
                                    pn.Row(
                                        plot_button,
                                        data_handler.upload_spinner3,
                                    )
                                    
                                ),
                                height = 750,
                            ),
                            pn.WidgetBox(
                                pn.pane.Markdown('## Line Plots',),
                                pn.Row(
                                    pn.WidgetBox(
                                        data_handler.x_dim_selector_lineplot,
                                        ),
                                    pn.WidgetBox(
                                        data_handler.y_dim_selector_lineplot,
                                    )                                ),
                                pn.WidgetBox(
                                    conditional_widget_line_plot,
                                ),
                                pn.WidgetBox(
                                    conditional_widget_line_plot2,
                                ), 
                                styles={'border': '1px solid #ccc', 'padding': '10px'},
                            ),
                            pn.WidgetBox(
                                pn.pane.Markdown('## Heat Maps',),
                                pn.Row(
                                    pn.WidgetBox(
                                        data_handler.x_dim_selector_heatmap,
                                        ),
                                    pn.WidgetBox(
                                        data_handler.y_dim_selector_heatmap,
                                    ),
                                    pn.WidgetBox(
                                        data_handler.z_dim_selector_heatmap,
                                    )
                                ),
                                # conditional_widget_heatmap,
                                styles={'border': '1px solid #ccc', 'padding': '10px'},
                                margin=(20, 0, 0, 0),
                            ),
                            pn.WidgetBox(
                                 pn.Card(
                                            save_sliced_data_path,
                                            pn.Column(
                                                    save_sliced_data_overwrite,
                                                    pn.Row(
                                                        save_sliced_data_button,
                                                        save_sliced_data_spinner,
                                                    ),
                                                    
                                                    styles = {"padding-bottom":"20px"},
                                                
                                            ),
                                            #save_sliced_data_message,
                                            title='Export Data',
                                            styles = {"padding":"20px"},
                                            collapsed=False,
                                        ),
                                        margin=(20, 0, 0, 0),
                            )
                        ),
                )
    return None



conditional_widget_box1 = pn.bind( show_widget_box1, data_handler.param.dataset1, data_handler.param.dataset2 )
conditional_widget_box2 = pn.bind( show_widget_box2, data_handler.param.dataset1, data_handler.param.dataset2 )
conditional_widget_line_plot = pn.bind(data_handler.plot_lineplot, data_handler.x_dim_selector_lineplot, data_handler.y_dim_selector_lineplot,data_handler.param.selected_indices)
conditional_widget_line_plot2 = pn.bind(data_handler.plot_lineplot2, data_handler.x_dim_selector_lineplot, data_handler.y_dim_selector_lineplot,data_handler.param.selected_indices2)


main_part = pn.Column(
                pn.Row(
                    pn.Column(
                        project_description,  
                        divider_descr,
                        pn.Row(
                            pn.WidgetBox(
                                instruction1,
                                upload_file1,
                                pn.Row(
                                    upload_button1,
                                    upload_spinner1,
                                ),
                                styles={"padding-right":'25px',"padding-bottom":'50px'},
                            ),
                            pn.WidgetBox(
                                instruction2,
                                upload_file2,
                                pn.Row(
                                    upload_button2,
                                    upload_spinner2,
                                ),
                                styles={"padding-left":'25px',"padding-bottom":'50px'},
                            ),
                            height=180,
                        ),
                    ),
                ),
                pn.Column(
                    conditional_widget_box1,
                    conditional_widget_box2,
                    
                ),                
            ),

# Attach the callback to the button click 
upload_button1.on_click(data_handler.upload_callback_1)  
upload_button2.on_click(data_handler.upload_callback_2) 
plot_button.on_click(data_handler.plotting_graphs)


template = pn.template.FastListTemplate(title="DIA Data Analyzer",main=main_part)
template.servable()