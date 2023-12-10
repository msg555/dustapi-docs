class enemy_base
################
  Extend this class to create a new type of script-backed enemy.
  
  See :ref:`trigger_base<class trigger_base>` documentation for discussion on
  member variables. 

  .. _method-enemy_base-init:

  \ **void**\  *init*\ (\ **script**\ @ s, \ **scriptenemy**\ @ self)

    Called after the enemy is constructed, passing the corresponding game
    :ref:`scriptenemy<class scriptenemy>` handle. 

  .. _method-enemy_base-on_add:

  \ **void**\  *on_add*\ ()

    Called after the entity has been added to the scene. 

  .. _method-enemy_base-on_remove:

  \ **void**\  *on_remove*\ ()

    Called after the entity has been removed from the scene. 

  .. _method-enemy_base-on_change_scale:

  \ **void**\  *on_change_scale*\ (\ **float**\  new_scale)

    Called when the scale of the object has changed and collisions should be
    updated. 

  .. _method-enemy_base-step:

  \ **void**\  *step*\ ()

    Called when the enemy is stepped. 

  .. _method-enemy_base-editor_step:

  \ **void**\  *editor_step*\ ()

    Called when the enemy is stepped while in editor mode. 

  .. _method-enemy_base-draw:

  \ **void**\  *draw*\ (\ **float**\  sub_frame)

    Do drawing related to the enemy. 

  .. _method-enemy_base-editor_draw:

  \ **void**\  *editor_draw*\ (\ **float**\  sub_frame)

    Do drawing in the editor related to the enemy trigger. 

  .. _method-enemy_base-editor_var_changed:

  \ **void**\  *editor_var_changed*\ (\ **var_info**\ @ info)

    Called when one of this enemy's variables is modified in the editor 

  .. _method-enemy_base-on_message:

  \ **void**\  *on_message*\ (\ **string**\  id, \ **message**\ @ msg)

    Called when a message has been sent to the entity with
    ``entity.send_message(id, @msg)``. 

