enum state_types
################

::

  enum state_types{
    st_idle=0,
    st_victory=1,
    st_run=2,
    st_skid=3,
    st_superskid=4,
    st_fall=5,
    st_land=6,
    st_hover=7,
    st_jump=8,
    st_dash=9,
    st_crouch_jump=10,
    st_wall_run=11,
    st_wall_grab=12,
    st_wall_grab_idle=13,
    st_wall_grab_release=14,
    st_roof_grab=15,
    st_roof_grab_idle=16,
    st_roof_run=17,
    st_slope_slide=18,
    st_raise=19,
    st_stun=20,
    st_stun_wall=21,
    st_stun_ground=22,
    st_slope_run=23,
    st_hop=24,
    st_spawn=25,
    st_fly=26,
    st_thanks_cleansed=27,
    st_idle_cleansed=28,
    st_idle_cleansed_thanks=29,
    st_fall_cleansed=30,
    st_land_cleansed=31,
    st_cleansed=32,
    st_block=33,
    st_wall_dash=34,
  };

enum attack_types
#################

::

  enum attack_types{
    attack_type_idle=0,
    attack_type_light=1,
    attack_type_heavy=2,
    attack_type_special=3,
  };

enum var_types
##############

::

  enum var_types{
    var_type_none=0,
    var_type_bool=1,
    var_type_int8=2,
    var_type_int16=3,
    var_type_int32=4,
    var_type_int64=5,
    var_type_float=6,
    var_type_string=7,
    var_type_array=8,
    var_type_struct=9,
    var_type_vec2=10,
    var_type_handle_array=11,
    var_type_handle_struct=12,
  }

enum col_type
#############

::

  enum col_type{
    col_type_enemy = 1,
    col_type_filth = 2,
    col_type_particle = 3,
    col_type_prop = 4,
    col_type_player = 5,
    col_type_spring = 6,
    col_type_hittable = 7,
    col_type_hitbox = 8,
    col_type_poi = 9,
    col_type_poi_area = 10,
    col_type_projectile = 11,
    col_type_camera_node = 12,
    col_type_emitter = 13,
    col_type_cleansed = 14,
    col_type_AI_controller = 15,
    col_type_trigger = 16,
    col_type_check_point = 17,
    col_type_level_boundary = 18,
    col_type_level_start = 19,
    col_type_trigger_area = 20,
    col_type_kill_zone = 21,
    col_type_null = 22,
  };

enum team_types
###############

::

  enum team_types{
    team_filth = 0,
    team_cleaner = 1,
    team_none = 2,
  };

enum level_types
################

::

  enum level_types {
    lt_normal = 0,
    lt_nexus = 1,
    lt_nexus_mp = 2,
    lt_tugofwar = 3,
    lt_survival = 4,
    lt_rush = 5,
    lt_dustmod = 6,
  };

enum controller_modes
#####################

::

  enum controller_modes {
    controller_mode_standard = 0,
    controller_mode_ispressed = 1,
    controller_mode_posedge = 2,
    controller_mode_negedge = 3,
    controller_mode_advanced = 4,
  };

enum hit_outcomes
#################

::

  enum hit_outcomes{
    ho_start = 0,
    ho_hit = 1,
    ho_miss = 2,
    ho_parry = 3,
    ho_unresolved = 4,
    ho_parry_hit,
    ho_canceled
  };

enum player_virtual_button
##########################

::

  enum player_virtual_button {
    VB_UP = 0,
    VB_DOWN = 1,
    VB_LEFT = 2,
    VB_RIGHT = 3,
    VB_LIGHT = 4,
    VB_HEAVY = 5,
    VB_JUMP = 6,
    VB_DASH = 7,
    VB_TAUNT = 8,
    VB_NETWORK_PLAYER = 9,
  };

enum global_virtual_button
##########################

::

  enum global_virtual_button {
    GVB_WHEEL_UP = 0,
    GVB_WHEEL_DOWN = 1,
    GVB_LEFT_CLICK = 2,
    GVB_RIGHT_CLICK = 3,
    GVB_MIDDLE_CLICK = 4,
    GVB_ESCAPE = 5,
    GVB_RETURN = 6,
    GVB_QUICKRESTART = 7,
    GVB_SPACE = 8,
    GVB_LEVEL_EDITOR = 9,
    GVB_SHIFT = 10,
    GVB_CONTROL = 11,
    GVB_ALT = 12,
    GVB_BACK = 13,
    GVB_UP_ARROW = 14,
    GVB_DOWN_ARROW = 15,
    GVB_LEFT_ARROW = 16,
    GVB_RIGHT_ARROW = 17,
    GVB_PLUS = 18,
    GVB_MINUS = 19,
    GVB_BRACKET_OPEN = 20,
    GVB_BRACKET_CLOSE = 21,
    GVB_DELETE = 22,
    GVB_EDITOR_AUX = 23,
  };

enum side_types
###############

::

  enum side_types {
    side_left = 0,
    side_right = 1,
    side_roof = 2,
    side_ground = 3,
  };

enum filth_types
################

::

  enum filth_types {
    filth_type_clean = 0,
    filth_type_dust = 1,
    filth_type_leaf = 2,
    filth_type_trash = 3,
    filth_type_slime = 4,
    filth_type_poly = 5,
    filth_type_none = 6,
    filth_type_default = 7,
  };

enum node_types
###############

::

  enum node_types {
    nt_temp = 0,
    nt_normal = 1,
    nt_detach = 2,
    nt_connect = 3,
    nt_interest = 4,
    nt_force_connect = 5,
  };

enum script_fx_level
####################

::

  enum script_fx_level {
    script_fx_level_off=0,
    script_fx_level_low=1,
    script_fx_level_medium=2,
    script_fx_level_high=3,
  };
