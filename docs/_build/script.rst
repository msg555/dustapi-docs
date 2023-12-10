.. _class-script:

class script
############
  The entry point - each script must have a single class named *script*. 

  .. _method-script-checkpoint_save:

  \ **void**\  *checkpoint_save*\ ()

    Called just prior to a checkpoint being saved. 

  .. _method-script-checkpoint_load:

  \ **void**\  *checkpoint_load*\ ()

    Called after a checkpoint has been loaded. All entities and prop objects
    will have been recreated and therefore existing handles will no longer
    refer to objects in the scene and should be requeried. 

  .. _method-script-checkpoint_save-2:

  \ **void**\  *checkpoint_save*\ (\ **int**\  player_index)

    Called when a player hits a checkpoint during multiplayer. 

  .. _method-script-checkpoint_load-2:

  \ **void**\  *checkpoint_load*\ (\ **int**\  player_index)

    Called when a player is respawned during multiplayer. 

  .. _method-script-entity_on_add:

  \ **void**\  *entity_on_add*\ (\ :ref:`entity<class-entity>`\ @ e)

    Called when an entity is added to the scene. This is called when an entity
    is explictly added to the scene, or when it is loaded in. 

  .. _method-script-entity_on_remove:

  \ **void**\  *entity_on_remove*\ (\ :ref:`entity<class-entity>`\ @ e)

    Called when an entity is removed from the scene. Unlike `entity_on_add`
    this is not called when an entity is unloaded. 

  .. _method-script-move_cameras:

  \ **void**\  *move_cameras*\ ()

    Called before the entity list to process has been constructed as an
    opportunity to move the camera. Moving the camera in
    \ :ref:`script.step<method-script-step>`\  will be too late to affect what segments
    and entities are loaded and stepped.
    

  .. _method-script-step:

  \ **void**\  *step*\ (\ **int**\  entities)

    Called every game frame (usually 60fps) prior to all entities having their step
    function called. The list of entities going to be stepped can be accessed
    with \ :ref:`entity_by_index<func-entity_by_index>`\ (i) for ``0 <= i < entities``.
    

  .. _method-script-step_post:

  \ **void**\  *step_post*\ (\ **int**\  entities)

    Like step except called after all entities have had their step functions
    called. 

  .. _method-script-step_fixed:

  \ **void**\  *step_fixed*\ ()

    This function is called at 60fps even when the game menu is opened,
    slowed during fade out, loading checkpoints, etc. This is still
    subject to manipulation from pausing/changing game speed with frame
    advance, however. This mirrors the behavior of the menu subsystem.
    

  .. _method-script-pre_draw:

  \ **void**\  *pre_draw*\ (\ **float**\  sub_frame)

    Setup the camera/transform prior to anything being drawn. Do not actually
    draw anything here. 

  .. _method-script-draw:

  \ **void**\  *draw*\ (\ **float**\  sub_frame)

    Do any drawing required by your script. This function should have no side
    effects outside of the draw calls it makes. 

  .. _method-script-editor_step:

  \ **void**\  *editor_step*\ ()

    Called each frame while in the editor instead of step/step_post. 

  .. _method-script-editor_pre_draw:

  \ **void**\  *editor_pre_draw*\ (\ **float**\  sub_frame)

    Called each pre draw frame while in the editor instead of pre_draw. 

  .. _method-script-editor_draw:

  \ **void**\  *editor_draw*\ (\ **float**\  sub_frame)

    Called each draw frame while in the editor instead of draw. 

  .. _method-script-editor_var_changed:

  \ **void**\  *editor_var_changed*\ (\ :ref:`var_info<class-var_info>`\ @ info)

    Called when one of this script's variables is modified in the editor 

  .. _method-script-editor_entity_on_create:

  \ **void**\  *editor_entity_on_create*\ (\ :ref:`entity<class-entity>`\ @ e)

    Called when an entity is placed in the editor. 

  .. _method-script-editor_entity_on_add:

  \ **void**\  *editor_entity_on_add*\ (\ :ref:`entity<class-entity>`\ @ e)

    Called when an entity is added to the scene in the editor, either by being
    placed or loaded in. 

  .. _method-script-editor_entity_on_remove:

  \ **void**\  *editor_entity_on_remove*\ (\ :ref:`entity<class-entity>`\ @ e)

    Called when an entity is removed from the scene in the editor. 

  .. _method-script-spawn_player:

  \ **void**\  *spawn_player*\ (\ :ref:`message<class-message>`\ @ msg)

    Spawn a player controllable. The following parameters will be set
    in the passed message:
    
    :float x: The x coordinate to spawn the player
    :float y: The y coordinate to spawn the player
    :int player: The player index of the player
    :string character: The character id of the selected player
      (e.g. "dustgirl")
    
    The following fields can be set to create your player object:
    
    :entity@ player: Set the spawned player controllable.
    
    

  .. _method-script-build_sprites:

  \ **void**\  *build_sprites*\ (\ :ref:`message<class-message>`\ @ msg)

    Used to set custom sprite data from embedded values. See
    \ :ref:`has_embed_value<func-has_embed_value>`\ () for more details on how
    to embed a value. Sprites should be in PNG format.
    
    For each sprite you wish to create add a string to the message with the
    desired sprite name as the key and the embed key as the value.
    Additionally you can specify custom "offset" coordinates into the sprite
    to define where the center of the sprite is (defaults to (0, 0)) by
    setting an int key of the form "sprite_name|offsetx" and
    "sprite_name|offsety".
    
    See https://gist.github.com/msg555/3aaa96428d964c1612b540c208c3ad1e for
    a complete example on how to embed, build, and use custom sprites.
    

  .. _method-script-build_sounds:

  \ **void**\  *build_sounds*\ (\ :ref:`message<class-message>`\ @ msg)

    Userd to set custom sound data from embedded values similar to
    :ref:`build_sprites()<method-script-build_sprites>`.
    
    For each sound you wish to create add a string to the message with the
    desired sound name as the key and the embed key as the value.
    Additionally you can specify a custom loop point (measured in samples at
    44.1 kHz) by setting an int key of the form "sound_name|loop".
    
    See https://gist.github.com/msg555/821c3aec14852e67fd15c7ec96a851f2 for
    a complete example of how to embed, build, and use custom sounds.
    

  .. _method-script-on_level_start:

  \ **void**\  *on_level_start*\ ()

    Called when the level begins play either by loading the level normally or
    by tabbing in from the editor. 

  .. _method-script-on_level_end:

  \ **void**\  *on_level_end*\ ()

    Called when an end condition for the level has been triggered and the
    replay is about to be uploaded. You may still modify plugin_score at
    this point. 

  .. _method-script-editor_loaded:

  \ **void**\  *editor_loaded*\ ()

    Called when entering editor mode. Only applicable to editor plugins 

  .. _method-script-editor_unloaded:

  \ **void**\  *editor_unloaded*\ ()

    Called before entering play mode. Only applicable to editor plugins 

