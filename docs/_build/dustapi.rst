.. _method-puts:

\ **void**\  *puts*\ (const \ **string**\  &in msg)

  Write a string to the console on its own line. 

.. _method-tputs:

\ **void**\  *tputs*\ (const \ **string**\  &in msg)

  Write a string to the console on its own line with an additional
  timestamp heading. 

.. _method-script_name:

\ **string**\  *script_name*\ ()

  Returns the name of this script. Script names are used as a way of
  identifiying scripts for use when working with script triggers/enemies. 

.. _method-is_playing:

\ **bool**\  *is_playing*\ ()

  Returns false in the editor and true in game 

.. _method-is_replay:

\ **bool**\  *is_replay*\ ()

  Returns true if a replay is being watched 

.. _method-editor_sync_vars_menu:

\ **void**\  *editor_sync_vars_menu*\ ()

  Use after changing persistent variables via script to update values in the script panel. 

.. _method-get_scene:

\ **scene**\ @ *get_scene*\ ()

  Return the current scene object.  This scene object will be valid for
  the entire execution of the script. 

.. _method-get_script:

\ **script_base**\ @ *get_script*\ ()

  Return the global script object associated with this script. For technical
  reasons the script must implement the "script_base" interface, otherwise
  this api will return null. 

.. _method-get_camera:

\ **camera**\ @ *get_camera*\ (\ **uint**\  player)

  Return the camera following player 'player'. Like the scene object this
  object never needs to be reloaded.
  
  Arguments:
    :player: The (0-indexed) player index to get the camera of.
  

.. _method-num_cameras:

\ **uint**\  *num_cameras*\ ()

  Returns the number of cameras/players currently active. 

.. _method-get_active_camera:

\ **camera**\ @ *get_active_camera*\ ()

  Get the camera that is currently being viewed. 

.. _method-get_active_player:

\ **int**\  *get_active_player*\ ()

  Get the player index that is currently being viewed. Shorthand for
  get_active_camera.player(). 

.. _method-controller_entity:

\ **entity**\ @ *controller_entity*\ (\ **uint**\  player)

  This is deprecated, use controller_controllable which returns the same
  result except cast as a controllable. 

.. _method-controller_controllable:

\ **controllable**\ @ *controller_controllable*\ (\ **uint**\  player)

  Return the entity being controlled by player 'player'. This object
  is no longer valid and should be requeried when a checkpoint is loaded.
  

.. _method-controller_entity-2:

\ **void**\  *controller_entity*\ (\ **uint**\  player, \ **controllable**\ @ pl)

  Change the controllable controlled by player 'player'. 

.. _method-reset_camera:

\ **void**\  *reset_camera*\ (\ **uint**\  player)

  Reset all camera state based on the player's current position. 

.. _method-player_name:

\ **string**\  *player_name*\ (\ **int**\  player)

  Get the player name for the player id. Defaults to "Player " + (player + 1)
  if not in networking mode or the player name is not known. Returns an empty
  string if the player does not exist. 

.. _method-entity_by_id:

\ **entity**\ @ *entity_by_id*\ (\ **uint**\  id)

  Return the entity with the given id. The returned entity object is no
  longer valid if the entity is removed from the scene either by being
  destroyed, unloaded, or a checkpoint is loaded. The safest thing to do
  is requery the entity every frame it will be used.
  
  This function will return null if the entity has been destroyed or is not
  currently loaded. 

.. _method-controllable_by_id:

\ **controllable**\ @ *controllable_by_id*\ (\ **uint**\  id)

  Convenience method for entity_by_id that tries to return a controllable. 

.. _method-dustman_by_id:

\ **dustman**\ @ *dustman_by_id*\ (\ **uint**\  id)

  Convenience method for entity_by_id that tries to return a dustman. 

.. _method-hitbox_by_id:

\ **hitbox**\ @ *hitbox_by_id*\ (\ **uint**\  id)

  Convenience method for entity_by_id that tries to return a hitbox. 

.. _method-scripttrigger_by_id:

\ **scripttrigger**\ @ *scripttrigger_by_id*\ (\ **uint**\  id)

  Convenience method for entity_by_id that tries to return a script
  trigger. 

.. _method-scriptenemy_by_id:

\ **scriptenemy**\ @ *scriptenemy_by_id*\ (\ **uint**\  id)

  Convenience method for entity_by_id that tries to return a script
  enemy. 

.. _method-prop_by_id:

\ **prop**\ @ *prop_by_id*\ (\ **uint**\  id)

.. _method-entity_by_index:

\ **entity**\ @ *entity_by_index*\ (\ **uint**\  index)

  Return the 'index'th entity that will be steped this frame. Should only
  be called from 'step' and 'step_post'. See * entity_by_id() for notes on
  liveness of this object. 

.. _method-srand:

\ **void**\  *srand*\ (\ **uint32**\  sd)

  Seed the random generator. 

.. _method-rand:

\ **uint32**\  *rand*\ ()

  Generate a random 30-bit number. 

.. _method-create_tileinfo:

\ **tileinfo**\ @ *create_tileinfo*\ ()

  Create an tileinfo structure. Defaults to a square virtual tile. 

.. _method-create_tilefilth:

\ **tilefilth**\ @ *create_tilefilth*\ ()

  Create a tilefilth structure. Defaults to no filth on any edge. 

.. _method-create_sprites:

\ **sprites**\ @ *create_sprites*\ ()

  Create a sprites object that can be used to draw sprites to the screen. 

.. _method-create_prop:

\ **prop**\ @ *create_prop*\ ()

  Create a prop. 

.. _method-create_entity:

\ **entity**\ @ *create_entity*\ (\ **string**\  type_name)

  Create an entity object of the given type.  See
  https://gist.github.com/msg555/dcdc9d0644a813259072fe7b1cbdac30 for a
  list of types that can be created. 

.. _method-create_textfield:

\ **textfield**\ @ *create_textfield*\ ()

  Create a new textfield that can be used to draw text to the screen. 

.. _method-create_scripttrigger:

\ **scripttrigger**\ @ *create_scripttrigger*\ (\ **trigger_base**\ @ obj)

  Create a new script trigger backed by the passed trigger_base object. 

.. _method-create_scriptenemy:

\ **scriptenemy**\ @ *create_scriptenemy*\ (\ **enemy_base**\ @ obj)

  Create a new script enemy backed by the passed enemy_base object. 

.. _method-create_message:

\ **message**\ @ *create_message*\ ()

  Create an empty message object. 

.. _method-create_hitbox:

\ **hitbox**\ @ *create_hitbox*\ (\ **controllable**\ @ owner, \ **float**\  activate_time, \ **float**\  x, \ **float**\  y, \ **float**\  top, \ **float**\  bottom, \ **float**\  left, \ **float**\  right)

  Create a hitbox object. Note that the entity is not automatically added
  to the scene. However, hitboxes do automatically remove themselves from the
  scene sometime after activated. Hitboxes cannot be persisted and should be
  added to the scene with persist set to false. 

.. _method-create_canvas:

\ **canvas**\ @ *create_canvas*\ (\ **bool**\  is_hud, \ **int**\  layer, \ **int**\  sub_layer)

.. _method-add_broadcast_receiver:

\ **void**\  *add_broadcast_receiver*\ (\ **string**\  id, \ **callback_base**\ @ obj, \ **string**\  methName)

  Add a callback to receive all broadcasted messages with the given id. If id
  is blank then this receiver will instead receive all messages. 

.. _method-broadcast_message:

\ **void**\  *broadcast_message*\ (\ **string**\  id, \ **message**\ @ msg)

  Send a message to all registered broadcast receivers. 

.. _method-has_embed_value:

\ **bool**\  *has_embed_value*\ (\ **string**\  key)

  Returns true if there is an embedded file associated with the passed key.
  
  To embed a file into a script use a declaration like
    const string EMBED_key = "file.dat"
  
  That will seach for the file "file.dat" in embed_src/ and then script_src/.
  The file data will then be available to be queried by this function,
  get_embed_value, and can be used as sprite data in build_sprites.
  

.. _method-get_embed_value:

\ **string**\  *get_embed_value*\ (\ **string**\  key)

  Returns the embedded file data associated with the passed key. See
  has_embed_value for more details on how to embed a value in a script. 

.. _method-load_embed:

\ **bool**\  *load_embed*\ (\ **string**\  key, \ **string**\  path)

  Add/replace the embed key with the file present at
  "content/plugins/embeds/" + path. Use forward slashes to represent
  path separation.
  
  Returns true if the path was legal and an embed was
  successfully loaded. If it returns false any existing embed with the same
  key is unmodified.
  

.. _method-timestamp_now:

\ **int**\  *timestamp_now*\ ()

  Return the current unix timestamp. 

.. _method-get_time_us:

\ **uint32**\  *get_time_us*\ ()

  Get the current microseconds. 

.. _method-localtime:

\ **timedate**\ @ *localtime*\ (\ **int**\  timestamp)

  Convert a timestamp to a timedate structure in the local timezone. 

.. _method-localtime-2:

\ **timedate**\ @ *localtime*\ ()

  Convert the current time to a timedate structure in the local timezone. 

.. _method-gmtime:

\ **timedate**\ @ *gmtime*\ (\ **int**\  timestamp)

  Convert a timestamp to a timedate structure in the UTC timezone. 

.. _method-gmtime-2:

\ **timedate**\ @ *gmtime*\ ()

  Convert the current time to a timedate structure in the UTC timezone. 

.. _method-get_editor_api:

\ **editor_api**\ @ *get_editor_api*\ ()

  Get editor api object if currently in editor mode. 

.. _method-get_input_api:

\ **input_api**\ @ *get_input_api*\ ()

  Get input api object if currently in editor mode. 

.. _method-get_nexus_api:

\ **nexus_api**\ @ *get_nexus_api*\ ()

  Get nexus api object if currently in nexus. 

class scene
###########
  API methods included here are globally accessible within a script. 

  .. _method-scene-map_name:

  \ **string**\  *map_name*\ ()

    Get the current level name. 

  .. _method-scene-level_type:

  \ **int**\  *level_type*\ ()

    Get the current level type. 

  .. _method-scene-save_checkpoint:

  \ **void**\  *save_checkpoint*\ (\ **int**\  x, \ **int**\  y, \ **bool**\  use_position)

    Trigger a checkpoint to be saved. Note that the checkpoint is only saved at
    the start of the next frame.
    If use_position is false (the default due to a bug and for backwards
    compatibility reasons) x and y are ignored and the player's current
    position is used instead. 

  .. _method-scene-save_checkpoint-2:

  \ **void**\  *save_checkpoint*\ (\ **int**\  x, \ **int**\  y)

    Trigger a checkpoint to be saved. Note that the checkpoint is only saved at
    the start of the next frame. 

  .. _method-scene-load_checkpoint:

  \ **void**\  *load_checkpoint*\ ()

    Trigger the last checkpoint to be loaded. If no checkpoint has been set
    yet the level will be reloaded. 

  .. _method-scene-get_checkpoint_x:

  \ **float**\  *get_checkpoint_x*\ (\ **int**\  player)

    Get the x coordinate for the identified player of where they should respawn
    on death. 

  .. _method-scene-get_checkpoint_y:

  \ **float**\  *get_checkpoint_y*\ (\ **int**\  player)

    Get the y coordinate for the identified player of where they should respawn
    on death. 

  .. _method-scene-get_tile:

  \ **tileinfo**\ @ *get_tile*\ (\ **int**\  x, \ **int**\  y)

    Get the tileinfo structure for the tile at the given position on
    layer 19. 

  .. _method-scene-get_tile-2:

  \ **tileinfo**\ @ *get_tile*\ (\ **int**\  x, \ **int**\  y, \ **int**\  layer)

    Get the tileinfo structure for the tile at the given position and layer. 

  .. _method-scene-set_tile:

  \ **void**\  *set_tile*\ (\ **int**\  x, \ **int**\  y, \ **int**\  layer, \ **bool**\  solid, \ **int16**\  type, \ **int16**\  spriteSet, \ **int16**\  spriteTile, \ **int16**\  palette)

    Overwrite a tile in the scene.  See tileinfo documentation for what each
    of these parameters mean.
    

  .. _method-scene-set_tile-2:

  \ **void**\  *set_tile*\ (\ **int**\  x, \ **int**\  y, \ **int**\  layer, \ **tileinfo**\ @ tile, \ **bool**\  updateEdges)

    Overwrite a tile in the scene using the passed tileinfo structure. 

  .. _method-scene-get_tile_filth:

  \ **tilefilth**\ @ *get_tile_filth*\ (\ **int**\  x, \ **int**\  y)

    Get the tilefilth structure for the tile at the given location.
    Filth includes all things that can be on a side of a tile,
    i.e. all dust types and all spike types. 

  .. _method-scene-set_tile_filth:

  \ **uint**\  *set_tile_filth*\ (\ **int**\  x, \ **int**\  y, \ **uint8**\  top, \ **uint8**\  bottom, \ **uint8**\  left, \ **uint8**\  right, \ **bool**\  affectSpikes, \ **bool**\  overwrite)

    Set the filth for a given tile position. See tilefilth documentation for
    a description of how to interpret the top/bottom/left/right fields. 

  .. _method-scene-set_tile_filth-2:

  \ **uint**\  *set_tile_filth*\ (\ **int**\  x, \ **int**\  y, \ **tilefilth**\ @ filth)

    Set the filth for a given tile position using a tilefilth object. 

  .. _method-scene-project_tile_filth:

  \ **uint**\  *project_tile_filth*\ (\ **float**\  x, \ **float**\  y, \ **float**\  baseWidth, \ **float**\  baseHeight, \ **uint8**\  type, \ **float**\  direction, \ **float**\  distance, \ **float**\  spreadAngle, \ **bool**\  top, \ **bool**\  bottom, \ **bool**\  left, \ **bool**\  right, \ **bool**\  affectSpikes, \ **bool**\  overwrite)

    Project filth onto surfaces using the same line of sight system that is
    used e.g. to clear dust with attacks. Roughly speaking, the projection will
    be applied to any tile edge with a center that's within 'distance' pixels
    from the rectangle centered at (x, y) with size (baseWidth, baseHeight) in
    the direction of 'direction' +/- spreadAngle.
    
    The top/bottom/left/right flags indicate which types of surfaces can be
    affected.  'affectSpikes' indicates if spieks should be overwritten,
    'overwrite' indicates if only edges with no filth should be affected.
    
    Affected tiles with have their edge type set to 'type'.  See tilefilth
    documentation for a description on how to interpret this value. 

  .. _method-scene-default_collision_layer:

  \ **int**\  *default_collision_layer*\ ()

    Returns the current default collision layer. Normally this will be layer
    19 unless modified. 

  .. _method-scene-default_collision_layer-2:

  \ **void**\  *default_collision_layer*\ (\ **int**\  layer)

    Sets the default collision layer. Note that this value is not persisted
    across checkpoints. It is up to the script to set the value appropriately
    after a checkpoint has been loaded.
    

  .. _method-scene-ray_cast_tiles:

  \ **raycast**\ @ *ray_cast_tiles*\ (\ **float**\  x1, \ **float**\  y1, \ **float**\  x2, \ **float**\  y2)

    Return information about the first tile surface hit from the ray starting
    at (x1, y1) going to (x2, y2). 

  .. _method-scene-ray_cast_tiles-2:

  \ **raycast**\ @ *ray_cast_tiles*\ (\ **float**\  x1, \ **float**\  y1, \ **float**\  x2, \ **float**\  y2, \ **raycast**\ @ result)

    Like the other ray_cast_tiles call except reuse the raycast object result.
    This avoids unnecessary allocations if you're making a lot of calls per
    frame. 

  .. _method-scene-raycast_ray_cast_tiles_ex:

  \ **raycast**\ @ *raycast_ray_cast_tiles_ex*\ (\ **float**\  x1, \ **float**\  y1, \ **float**\  x2, \ **float**\  y2, \ **uint**\  layer)

    Like the other ray_cast_tiles except provide a layer. 

  .. _method-scene-ray_cast_tiles_ex:

  \ **raycast**\ @ *ray_cast_tiles_ex*\ (\ **float**\  x1, \ **float**\  y1, \ **float**\  x2, \ **float**\  y2, \ **uint**\  layer, \ **raycast**\ @ result)

    Like the other ray_cast_tiles except provide a layer. 

  .. _method-scene-ray_cast_tiles-3:

  \ **raycast**\ @ *ray_cast_tiles*\ (\ **float**\  x1, \ **float**\  y1, \ **float**\  x2, \ **float**\  y2, \ **int**\  edges)

    Return information about the first tile surface hit from the ray starting
    at (x1, y1) going to (x2, y2). 'edges' is a bitset indicating which types
    of edges it should look for collisions with. The 1, 2, 4, and 8 bits
    correspond to the top, bottom, left, and right edges respectively.
    
    Note that the game loads in data for about a 528x528 tile square centered
    around the camera (multiplayer uses a 144x144 square). Querying anything
    outside of this loaded region will give no results. 

  .. _method-scene-ray_cast_tiles-4:

  \ **raycast**\ @ *ray_cast_tiles*\ (\ **float**\  x1, \ **float**\  y1, \ **float**\  x2, \ **float**\  y2, \ **int**\  edges, \ **raycast**\ @ result)

    Like the other ray_cast_tiles call except reuse the raycast object result.
    This avoids unnecessary allocations if you're making a lot of calls per
    frame. 

  .. _method-scene-ray_cast_tiles_ex-2:

  \ **raycast**\ @ *ray_cast_tiles_ex*\ (\ **float**\  x1, \ **float**\  y1, \ **float**\  x2, \ **float**\  y2, \ **int**\  edges, \ **uint**\  layer)

    Like the other ray_cast_tiles except provide a layer. 

  .. _method-scene-ray_cast_tiles_ex-3:

  \ **raycast**\ @ *ray_cast_tiles_ex*\ (\ **float**\  x1, \ **float**\  y1, \ **float**\  x2, \ **float**\  y2, \ **int**\  edges, \ **uint**\  layer, \ **raycast**\ @ result)

    Like the other ray_cast_tiles except provide a layer. 

  .. _method-scene-collision_ground:

  \ **tilecollision**\ @ *collision_ground*\ (\ **float**\  x1, \ **float**\  y1, \ **float**\  x2, \ **float**\  y2)

    Find the collision of the horizontal line segment (x1, y1), (x2, y1) with
    tiles as it moves downward to y2. Only collides with ground edges. 

  .. _method-scene-collision_roof:

  \ **tilecollision**\ @ *collision_roof*\ (\ **float**\  x1, \ **float**\  y1, \ **float**\  x2, \ **float**\  y2)

    Find the collision of the horizontal line segment (x1, y1), (x2, y1) with
    tiles as it moves upward to y2. Only collides with roof edges. 

  .. _method-scene-collision_left:

  \ **tilecollision**\ @ *collision_left*\ (\ **float**\  x1, \ **float**\  y1, \ **float**\  x2, \ **float**\  y2)

    Find the collision of the vertical line segment (x1, y1), (x1, y2) with
    tiles as it moves leftward to x2. Only collides with left edges. 

  .. _method-scene-collision_right:

  \ **tilecollision**\ @ *collision_right*\ (\ **float**\  x1, \ **float**\  y1, \ **float**\  x2, \ **float**\  y2)

    Find the collision of the vertical line segment (x1, y1), (x1, y2) with
    tiles as it moves rightward to x2. Only collides with right edges. 

  .. _method-scene-collision_ground_ex:

  \ **tilecollision**\ @ *collision_ground_ex*\ (\ **float**\  x1, \ **float**\  y1, \ **float**\  x2, \ **float**\  y2, \ **uint**\  layer)

    Like collision_ground except provide a layer. 

  .. _method-scene-collision_roof_ex:

  \ **tilecollision**\ @ *collision_roof_ex*\ (\ **float**\  x1, \ **float**\  y1, \ **float**\  x2, \ **float**\  y2, \ **uint**\  layer)

    Like collision_roof except provide a layer. 

  .. _method-scene-collision_left_ex:

  \ **tilecollision**\ @ *collision_left_ex*\ (\ **float**\  x1, \ **float**\  y1, \ **float**\  x2, \ **float**\  y2, \ **uint**\  layer)

    Like collision_left except provide a layer. 

  .. _method-scene-collision_right_ex:

  \ **tilecollision**\ @ *collision_right_ex*\ (\ **float**\  x1, \ **float**\  y1, \ **float**\  x2, \ **float**\  y2, \ **uint**\  layer)

    Like collision_right except provide a layer. 

  .. _method-scene-get_entity_collision:

  \ **int**\  *get_entity_collision*\ (\ **float**\  top, \ **float**\  bottom, \ **float**\  left, \ **float**\  right, \ **uint**\  type)

    Get all the entity collisions of a given type in the rectangle. 'type'
    should be an element from the col_type enum at the bottom of this
    documentation. The return value is the number of collisions found. Use
    get_entity_collision_index to query the index'th result. 

  .. _method-scene-get_entity_collision_index:

  \ **entity**\ @ *get_entity_collision_index*\ (\ **uint**\  index)

    Returns the index'th entity from the last `get_..._collision` call. 

  .. _method-scene-get_controllable_collision_index:

  \ **controllable**\ @ *get_controllable_collision_index*\ (\ **uint**\  index)

    Convenience method for get_entitiy_collision_index that tries to return a
    controllable. 

  .. _method-scene-get_dustman_collision_index:

  \ **dustman**\ @ *get_dustman_collision_index*\ (\ **uint**\  index)

    Convenience method for get_entitiy_collision_index that tries to return a
    dustman. 

  .. _method-scene-get_hitbox_collision_index:

  \ **hitbox**\ @ *get_hitbox_collision_index*\ (\ **uint**\  index)

    Convenience method for get_entitiy_collision_index that tries to return a
    hitbox. 

  .. _method-scene-get_scripttrigger_collision_index:

  \ **scripttrigger**\ @ *get_scripttrigger_collision_index*\ (\ **uint**\  index)

    Convenience method for get_entitiy_collision_index that tries to
    return a script trigger. 

  .. _method-scene-get_scriptenemy_collision_index:

  \ **scriptenemy**\ @ *get_scriptenemy_collision_index*\ (\ **uint**\  index)

    Convenience method for get_entitiy_collision_index that tries to
    return a script enemy. 

  .. _method-scene-get_prop_collision:

  \ **int**\  *get_prop_collision*\ (\ **float**\  top, \ **float**\  bottom, \ **float**\  left, \ **float**\  right)

    Get all the prop collisions within the query rectangle. The return value is
    the number of prop collisions detected. Use get_prop_collision_index to
    query the index'th result. 

  .. _method-scene-get_prop_collision_index:

  \ **prop**\ @ *get_prop_collision_index*\ (\ **uint**\  index)

    Returns the index'th prop from the last `get_..._collision` call. 

  .. _method-scene-override_stream_sizes:

  \ **void**\  *override_stream_sizes*\ (\ **int**\  load_size, \ **int**\  step_size)

    Override the default stream sizes. Stream sizes are measured in segments
    (16x16 tile squares). The streaming area is a square region of segments
    with side length given by the stream size.
    
    Constraints:
      `8 <= step_size <= load_size <= 256`
    
    Arguments:
      :load_size: Controls when entities are loaded into memory and
        written back to persist.
    
      :step_size: Controls when an entitie's logic will be executed.
    

  .. _method-scene-combo_break_count:

  \ **int**\  *combo_break_count*\ ()

    Returns the number of combo breaks that have been recorded for the current
    replay. This translates to finess scores as 0=S, 1=A, 2-3=B, 4-5=C, 6+=D 

  .. _method-scene-combo_break_count-2:

  \ **void**\  *combo_break_count*\ (\ **int**\  combo_break_count)

    Set the current combo break count. 

  .. _method-scene-add_prop:

  \ **void**\  *add_prop*\ (\ **prop**\ @ prop)

    Add a prop into the scene to be rendered each frame. 

  .. _method-scene-remove_prop:

  \ **void**\  *remove_prop*\ (\ **prop**\ @ prop)

    Remove a prop from the scene. 

  .. _method-scene-add_entity:

  \ **void**\  *add_entity*\ (\ **entity**\ @ entity)

    Add an entity to the scene to be step'ed and drawn. 

  .. _method-scene-add_entity-2:

  \ **void**\  *add_entity*\ (\ **entity**\ @ entity, \ **bool**\  persist)

    Add an entity to the scene to be step'ed and drawn. 'persist' indicates if
    the entity should be saved and loaded using the checkpoint system. 

  .. _method-scene-remove_entity:

  \ **void**\  *remove_entity*\ (\ **entity**\ @ entity)

    Remove an entity from the scene. 

  .. _method-scene-layer_visible:

  \ **bool**\  *layer_visible*\ (\ **uint**\  layer)

    Access the visibility of each layer. 

  .. _method-scene-layer_visible-2:

  \ **void**\  *layer_visible*\ (\ **uint**\  layer, \ **bool**\  visible)

  .. _method-scene-layer_scale:

  \ **float**\  *layer_scale*\ (\ **uint**\  layer)

    Access the scaling factor of the layer. 1.0 is the standard foreground
    scale with lower values being used for the background. 

  .. _method-scene-layer_scale-2:

  \ **void**\  *layer_scale*\ (\ **uint**\  layer, \ **float**\  scale)

  .. _method-scene-reset_layer_order:

  \ **void**\  *reset_layer_order*\ ()

    Reset the render order of the layers to the default. 

  .. _method-scene-swap_layer_order:

  \ **void**\  *swap_layer_order*\ (\ **uint**\  layer1, \ **uint**\  layer2)

    Swap the rendering order of two layers. Note that this only changes the
    order that draw commands are applied and does not affect other layer
    attributes like fog colour or scale.
    
    Note that layer order is not persisted across checkpoints. It is up to
    the script to set the layer ordering appropriately after a checkpoint is
    loaded.
    

  .. _method-scene-get_layer_position:

  \ **uint**\  *get_layer_position*\ (\ **uint**\  layer)

    Get the render position of a layer. Normally this is just the layer index
    itself unless swap_layer_order has been used.
    

  .. _method-scene-draw_rectangle_world:

  \ **void**\  *draw_rectangle_world*\ (\ **uint**\  layer, \ **uint**\  sub_layer, \ **float**\  x1, \ **float**\  y1, \ **float**\  x2, \ **float**\  y2, \ **float**\  rotation, \ **uint**\  colour)

    Draw a rectangle in the world scene's coordinates. colour is an ARGB value
    in big endian byte order (alpha is the high byte). 

  .. _method-scene-draw_glass_world:

  \ **void**\  *draw_glass_world*\ (\ **uint**\  layer, \ **uint**\  sub_layer, \ **float**\  x1, \ **float**\  y1, \ **float**\  x2, \ **float**\  y2, \ **float**\  rotation, \ **uint**\  colour)

    Like draw rectangle except a blur shader is used. 

  .. _method-scene-draw_gradient_world:

  \ **void**\  *draw_gradient_world*\ (\ **uint**\  layer, \ **uint**\  sub_layer, \ **float**\  x1, \ **float**\  y1, \ **float**\  x2, \ **float**\  y2, \ **uint**\  c00, \ **uint**\  c10, \ **uint**\  c11, \ **uint**\  c01)

    Draws a gradient to the screen like how the background is drawn. 

  .. _method-scene-draw_line:

  \ **void**\  *draw_line*\ (\ **uint**\  layer, \ **uint**\  sub_layer, \ **float**\  x1, \ **float**\  y1, \ **float**\  x2, \ **float**\  y2, \ **float**\  width, \ **uint**\  colour)

    Deprecated, use draw_line_world instead. 

  .. _method-scene-draw_line_world:

  \ **void**\  *draw_line_world*\ (\ **uint**\  layer, \ **uint**\  sub_layer, \ **float**\  x1, \ **float**\  y1, \ **float**\  x2, \ **float**\  y2, \ **float**\  width, \ **uint**\  colour)

    Draws a line between the two points. 

  .. _method-scene-draw_quad_world:

  \ **void**\  *draw_quad_world*\ (\ **uint**\  layer, \ **uint**\  sub_layer, \ **bool**\  is_glass, \ **float**\  x1, \ **float**\  y1, \ **float**\  x2, \ **float**\  y2, \ **float**\  x3, \ **float**\  y3, \ **float**\  x4, \ **float**\  y4, \ **uint**\  c1, \ **uint**\  c2, \ **uint**\  c3, \ **uint**\  c4)

    Generic call to draw an arbitrary quadralateral. Specify points in counter
    clockwise order. Glass is not actually supported and so is_glass is
    currently ignored.
    
    The engine draws quads under the hood by drawing two triangles between
    points (1, 2, 3) and points (1, 3, 4).  Note that this means that the color
    at points 1 and 3 bleed into both halfs while the colors at points 2 and 4
    are restricted to just one half.
    

  .. _method-scene-draw_rectangle_hud:

  \ **void**\  *draw_rectangle_hud*\ (\ **uint**\  layer, \ **uint**\  sub_layer, \ **float**\  x1, \ **float**\  y1, \ **float**\  x2, \ **float**\  y2, \ **float**\  rotation, \ **uint**\  colour)

    Analagous draw routines for the hud coordinate space. To scripts the hud is
    a 1600 by 900 pixel rectangle centered at the origin. 

  .. _method-scene-draw_glass_hud:

  \ **void**\  *draw_glass_hud*\ (\ **uint**\  layer, \ **uint**\  sub_layer, \ **float**\  x1, \ **float**\  y1, \ **float**\  x2, \ **float**\  y2, \ **float**\  rotation, \ **uint**\  colour)

  .. _method-scene-draw_gradient_hud:

  \ **void**\  *draw_gradient_hud*\ (\ **uint**\  layer, \ **uint**\  sub_layer, \ **float**\  x1, \ **float**\  y1, \ **float**\  x2, \ **float**\  y2, \ **uint**\  c00, \ **uint**\  c10, \ **uint**\  c11, \ **uint**\  c01)

  .. _method-scene-draw_line_hud:

  \ **void**\  *draw_line_hud*\ (\ **uint**\  layer, \ **uint**\  sub_layer, \ **float**\  x1, \ **float**\  y1, \ **float**\  x2, \ **float**\  y2, \ **float**\  width, \ **uint**\  colour)

  .. _method-scene-draw_quad_hud:

  \ **void**\  *draw_quad_hud*\ (\ **uint**\  layer, \ **uint**\  sub_layer, \ **bool**\  is_glass, \ **float**\  x1, \ **float**\  y1, \ **float**\  x2, \ **float**\  y2, \ **float**\  x3, \ **float**\  y3, \ **float**\  x4, \ **float**\  y4, \ **uint**\  c1, \ **uint**\  c2, \ **uint**\  c3, \ **uint**\  c4)

    Generic call to draw an arbitrary quadralateral. Specify points in counter
    clockwise order. is_glass is not supported and is ignored.
    
    The engine draws quads under the hood by drawing two triangles between
    points (1, 2, 3) and points (1, 3, 4).  Note that this means that the color
    at points 1 and 3 bleed into both halfs while the colors at points 2 and 4
    are restricted to just one half.
    

  .. _method-scene-disable_score_overlay:

  \ **void**\  *disable_score_overlay*\ (\ **bool**\  disable_overlay)

    Prevent the normal score overlay (including the combo, combo-meter, and
    time displays) from rendering. 

  .. _method-scene-play_sound:

  \ **audio**\ @ *play_sound*\ (\ **string**\  name, \ **float**\  x, \ **float**\  y, \ **float**\  volume, \ **bool**\  loop, \ **bool**\  positional)

    See https://gist.github.com/msg555/46f46b8b943ee93393a0a192c7703c57
    for a list of sound and stream names to use. 

  .. _method-scene-play_stream:

  \ **audio**\ @ *play_stream*\ (\ **string**\  name, \ **uint**\  soundGroup, \ **float**\  x, \ **float**\  y, \ **bool**\  loop, \ **float**\  volume)

    'soundGroup' determines which global volume slider to apply to this sound.
    1 for music, 2 for ambience, and anything else is considered a sound
    effect. 

  .. _method-scene-play_script_stream:

  \ **audio**\ @ *play_script_stream*\ (\ **string**\  name, \ **uint**\  soundGroup, \ **float**\  x, \ **float**\  y, \ **bool**\  loop, \ **float**\  volume)

    Play a stream that was loaded in using the script.build_sounds() callback.
    

  .. _method-scene-play_persistent_stream:

  \ **audio**\ @ *play_persistent_stream*\ (\ **string**\  name, \ **uint**\  sound_group, \ **bool**\  loop, \ **float**\  volume, const \ **bool**\  script_sound)

    Play a sound that will continue to play after a reset, similar to in game music.
    If the specified audio is already playing nothing will happen.
    script_sound indicates if the sound to be played is a script, or built in sound.
    Note that calling audio.stop() on the returned audio won't automatically remove it from
    the script music registry, use scene.stop_persistent_stream instead.
    

  .. _method-scene-stop_persistent_stream:

  \ **bool**\  *stop_persistent_stream*\ (\ **string**\  name)

    Returns true if the specified persistent stream was stopped.
    

  .. _method-scene-get_persistent_stream:

  \ **audio**\ @ *get_persistent_stream*\ (\ **string**\  name)

    Returns the specified persitent sound if it is playing, or null otherwise. 

  .. _method-scene-override_sound:

  \ **void**\  *override_sound*\ (\ **string**\  sound, \ **string**\  override_sound, \ **bool**\  script_sound)

    Overrides the built in sound named "sound" with "override_sound".
    Any time the game tries to play that sound, the override will be played instead.
    script_sound indicates whether an embedded, or built in sound will be used for the override 

  .. _method-scene-has_sound_override:

  \ **bool**\  *has_sound_override*\ (\ **string**\  sound)

    Returns true if the sound has been overridden 

  .. _method-scene-get_sound_override:

  \ **string**\  *get_sound_override*\ (\ **string**\  sound)

    Returns the override for the specified sound, or an empty string 

  .. _method-scene-is_sound_override_script:

  \ **bool**\  *is_sound_override_script*\ (\ **string**\  sound)

    Returns true if the specified override uses a script sound 

  .. _method-scene-clear_sound_override:

  \ **void**\  *clear_sound_override*\ (\ **string**\  sound)

    Clears the specified sound overrides if there is one 

  .. _method-scene-clear_sound_overrides:

  \ **void**\  *clear_sound_overrides*\ ()

    Clears all sound overrides 

  .. _method-scene-add_collision:

  \ **collision**\ @ *add_collision*\ (\ **entity**\ @ e, \ **float**\  top, \ **float**\  bottom, \ **float**\  left, \ **float**\  right, \ **uint32**\  collision_type)

    Insert a new collision object into the scene. 

  .. _method-scene-mouse_x_hud:

  \ **float**\  *mouse_x_hud*\ (\ **int**\  player, \ **bool**\  scale)

    Returns the x coordinate of the mouse in the hud coordinate space. If scale
    is set to true will auto scale the coordinates to simulate a 1600-900
    screen size. Will range between -width/2 and width/2.
    

  .. _method-scene-mouse_x_hud-2:

  \ **float**\  *mouse_x_hud*\ (\ **int**\  player)

    Equivalent to mouse_x_hud(player, true) 

  .. _method-scene-mouse_y_hud:

  \ **float**\  *mouse_y_hud*\ (\ **int**\  player, \ **bool**\  scale)

    Returns the y coordinate of the mouse in the hud coordinate space. If scale
    is set to true will auto scale the coordinates to simulate a 1600-900
    screen size. Will range between -height/2 and height/2.
    

  .. _method-scene-mouse_y_hud-2:

  \ **float**\  *mouse_y_hud*\ (\ **int**\  player)

    Equivalent to mouse_y_hud(player, true) 

  .. _method-scene-mouse_x_world:

  \ **float**\  *mouse_x_world*\ (\ **int**\  player, \ **int**\  layer)

    Returns the x coordinate of the mouse for the given player's camera in the
    given layer. 

  .. _method-scene-mouse_y_world:

  \ **float**\  *mouse_y_world*\ (\ **int**\  player, \ **int**\  layer)

    Returns the y coordinate of the mouse for the given player's camera in the
    given layer. 

  .. _method-scene-hud_screen_width:

  \ **float**\  *hud_screen_width*\ (\ **bool**\  scale)

    Return the current HUD screen width in pixels. If scale is true this
    always returns 1600. 

  .. _method-scene-hud_screen_height:

  \ **float**\  *hud_screen_height*\ (\ **bool**\  scale)

    Return the current HUD screen height in pixels. If scale is true this
    always returns 900. 

  .. _method-scene-mouse_state:

  \ **int**\  *mouse_state*\ (\ **int**\  player)

    Returns the mouse state for the given player as a bitmask. See the below
    table for what button each bit corresponds to.
    
    Arguments:
      :player: the player to get input for
    
    Bitmask:
      :1: wheel up
      :2: wheel down
      :4: left click
      :8: right click
      :16: middle click
    

  .. _method-scene-end_level:

  \ **void**\  *end_level*\ (\ **float**\  x, \ **float**\  y)

    Trigger the level to be ended. Note that the replay won't actually end
    until the next frame if the frame has already begun. (x, y) are the respawn
    location if the player dies. 

  .. _method-scene-plugin_score:

  \ **int**\  *plugin_score*\ ()

    Access the plugin score used to add an extra criteria for ranks on
    leaderboards (only) when plugins are used. Lower scores rank better.
    The Score leaderboard is ranked by
    (completion, plugin_score, finesse, time) while the Time leaderboard is
    ranked by (plugin_score, time, completion + finesse).
    
    The score is restricted to the rank [0, 1000].
    
    Note that this field does nothing when the player isn't using a plugin. 

  .. _method-scene-plugin_score-2:

  \ **void**\  *plugin_score*\ (\ **int**\  plugin_score)

  .. _method-scene-add_effect:

  \ **entity**\ @ *add_effect*\ (\ **string**\  sprite_set, \ **string**\  sprite_name, \ **float**\  x, \ **float**\  y, \ **float**\  rotation, \ **float**\  scale_x, \ **float**\  scale_y, \ **float**\  frame_rate)

    Create a new effect based off a sprite animation. 

  .. _method-scene-add_follow_effect:

  \ **entity**\ @ *add_follow_effect*\ (\ **string**\  sprite_set, \ **string**\  sprite_name, \ **float**\  x, \ **float**\  y, \ **float**\  rotation, \ **float**\  scale_x, \ **float**\  scale_y, \ **float**\  frame_rate, \ **entity**\ @ follow, \ **bool**\  follow_x, \ **bool**\  follow_y)

    Create a new effect based off a sprite animation that follows an entity.
    
    follow_x indicates that the effect x coordinate should be computed as
    follow.x + x. follow_y means similar for y coordinates. If follow_x and
    follow_y are both false then this behaves the same as add_effect.
    

  .. _method-scene-get_filth_level:

  \ **void**\  *get_filth_level*\ (\ **int**\  &out filth, \ **int**\  &out filth_block, \ **int**\  &out enemy)

    Writes the total initial amount of filth, dustblocks, and enemy life
    in the level to the passed variables.
    

  .. _method-scene-get_filth_remaining:

  \ **void**\  *get_filth_remaining*\ (\ **int**\  &out filth, \ **int**\  &out filth_block, \ **int**\  &out enemy)

    Writes the current amount of filth, dustblocks, and enemy life
    in the level to the passed variables.
    

  .. _method-scene-time_warp:

  \ **float**\  *time_warp*\ ()

    The time warp field can be used to dilate time. e.g. a time_warp of
    0.5 will make the world scene run in half time.
    

  .. _method-scene-time_warp-2:

  \ **void**\  *time_warp*\ (\ **float**\  time_warp)

class rectangle
###############
  .. _method-rectangle-top:

  \ **float**\  *top*\ ()

  .. _method-rectangle-top-2:

  \ **void**\  *top*\ (\ **float**\  _top)

  .. _method-rectangle-bottom:

  \ **float**\  *bottom*\ ()

  .. _method-rectangle-bottom-2:

  \ **void**\  *bottom*\ (\ **float**\  _bottom)

  .. _method-rectangle-left:

  \ **float**\  *left*\ ()

  .. _method-rectangle-left-2:

  \ **void**\  *left*\ (\ **float**\  _left)

  .. _method-rectangle-right:

  \ **float**\  *right*\ ()

  .. _method-rectangle-right-2:

  \ **void**\  *right*\ (\ **float**\  _right)

  .. _method-rectangle-get_width:

  \ **float**\  *get_width*\ ()

  .. _method-rectangle-get_height:

  \ **float**\  *get_height*\ ()

class raycast
#############
  Represents a ray cast result. 

  .. _method-raycast-hit:

  \ **bool**\  *hit*\ ()

    Returns true if the ray cast hit a tile. 

  .. _method-raycast-tile_x:

  \ **int**\  *tile_x*\ ()

    Returns the (tile) coordinates of the hit tile. 

  .. _method-raycast-tile_y:

  \ **int**\  *tile_y*\ ()

  .. _method-raycast-hit_x:

  \ **float**\  *hit_x*\ ()

    Returns the coordinates pixel coordinates where the ray actually intersects
    the tile face. 

  .. _method-raycast-hit_y:

  \ **float**\  *hit_y*\ ()

  .. _method-raycast-tile_side:

  \ **int**\  *tile_side*\ ()

    Returns 0-3 indicating the side of the edge hit from
    top, bottom, left, right in that order. 

  .. _method-raycast-angle:

  \ **int**\  *angle*\ ()

    Returns the angle of hit tile surface. 

class tilecollision
###################
  .. _method-tilecollision-reset:

  \ **void**\  *reset*\ ()

  .. _method-tilecollision-hit:

  \ **bool**\  *hit*\ ()

  .. _method-tilecollision-hit-2:

  \ **void**\  *hit*\ (\ **bool**\  is_solid)

  .. _method-tilecollision-hit_x:

  \ **float**\  *hit_x*\ ()

  .. _method-tilecollision-hit_x-2:

  \ **void**\  *hit_x*\ (\ **float**\  outside_x)

  .. _method-tilecollision-hit_y:

  \ **float**\  *hit_y*\ ()

  .. _method-tilecollision-hit_y-2:

  \ **void**\  *hit_y*\ (\ **float**\  outside_y)

  .. _method-tilecollision-angle:

  \ **float**\  *angle*\ ()

  .. _method-tilecollision-type:

  \ **int**\  *type*\ ()

  .. _method-tilecollision-type-2:

  \ **void**\  *type*\ (\ **int**\  type)

class tileinfo
##############
  Represents what tile shape and sprite is present at a tile and which edges
  have collisions. Does not include filth information. 

  .. _method-tileinfo-type:

  \ **uint8**\  *type*\ ()

    See the notes in the TileShape class at
    https://github.com/msg555/dustmaker/blob/master/dustmaker/Tile.py
    for how the `type` parameter maps to the shape of the tile.
    
    See C's diagram for an illustration of the different tile types.
    https://github.com/cmann1/PropUtils/blob/master/files/tiles_reference/TileShapes.jpg
    

  .. _method-tileinfo-type-2:

  \ **void**\  *type*\ (\ **int**\  _type)

  .. _method-tileinfo-solid:

  \ **bool**\  *solid*\ ()

    Indicates whether a tile is present. The rest of the fields are irrelevant
    if solid is set to false. 

  .. _method-tileinfo-solid-2:

  \ **void**\  *solid*\ (\ **bool**\  _solid)

  .. _method-tileinfo-angle:

  \ **int32**\  *angle*\ ()

    Angle is a function of the type 'type'. It indicates the angle
    that the non-flat edge is oriented. A square tile (type 0) has
    an angle of 0. 

  .. _method-tileinfo-sprite_set:

  \ **uint8**\  *sprite_set*\ ()

    See C's reference on the different available sprite set/tile/palettes
    available.
    
    https://github.com/cmann1/PropUtils/blob/master/tile-data.json
    https://github.com/cmann1/PropUtils/tree/master/files/tiles_reference
    

  .. _method-tileinfo-sprite_set-2:

  \ **void**\  *sprite_set*\ (\ **int**\  _sprite_set)

  .. _method-tileinfo-sprite_tile:

  \ **uint8**\  *sprite_tile*\ ()

  .. _method-tileinfo-sprite_tile-2:

  \ **void**\  *sprite_tile*\ (\ **uint8**\  _sprite_tile)

  .. _method-tileinfo-sprite_palette:

  \ **uint8**\  *sprite_palette*\ ()

  .. _method-tileinfo-sprite_palette-2:

  \ **void**\  *sprite_palette*\ (\ **uint8**\  _sprite_palette)

  .. _method-tileinfo-edge_top:

  \ **uint8**\  *edge_top*\ ()

    Each tile edge is represented by four bits. These are their meanings from
    least significant bit to most significant bit.
    
    1 bit - indicates edge "priority"?
    2 bit - whether to draw an edge cap on the left/top.
    4 bit - whether to draw an edge cap on the right/bottom.
    8 bit - indicates whether the edge has collision and can have filth.
    

  .. _method-tileinfo-edge_top-2:

  \ **void**\  *edge_top*\ (\ **uint8**\  _edge_top)

  .. _method-tileinfo-edge_bottom:

  \ **uint8**\  *edge_bottom*\ ()

  .. _method-tileinfo-edge_bottom-2:

  \ **void**\  *edge_bottom*\ (\ **uint8**\  _edge_bottom)

  .. _method-tileinfo-edge_left:

  \ **uint8**\  *edge_left*\ ()

  .. _method-tileinfo-edge_left-2:

  \ **void**\  *edge_left*\ (\ **uint8**\  _edge_left)

  .. _method-tileinfo-edge_right:

  \ **uint8**\  *edge_right*\ ()

  .. _method-tileinfo-edge_right-2:

  \ **void**\  *edge_right*\ (\ **uint8**\  _edge_right)

  .. _method-tileinfo-is_dustblock:

  \ **bool**\  *is_dustblock*\ ()

    Returns true if the tile is a dustblock tile. 

  .. _method-tileinfo-set_dustblock:

  \ **void**\  *set_dustblock*\ (\ **int**\  _sprite_set)

    Set the tile's sprite_tile and sprite_palette parameters to be the
    dustblock tile type in the given sprite set. 

class tilefilth
###############
  Describes the filth or spikes on a tile. 

  .. _method-tilefilth-top:

  \ **uint8**\  *top*\ ()

    Each tile filth value indicates if and what type of filth or spikes are
    present on a given face of a tile.  These values should be:
    
    0: no filth/spikes
    1-5: dust, leaves, trash, slime, virtual filth
    9-13: mansion spikes, forest spikes, cones, wires, virtual spikes
    

  .. _method-tilefilth-top-2:

  \ **void**\  *top*\ (\ **uint8**\  _top)

  .. _method-tilefilth-bottom:

  \ **uint8**\  *bottom*\ ()

  .. _method-tilefilth-bottom-2:

  \ **void**\  *bottom*\ (\ **uint8**\  _bottom)

  .. _method-tilefilth-left:

  \ **uint8**\  *left*\ ()

  .. _method-tilefilth-left-2:

  \ **void**\  *left*\ (\ **uint8**\  _left)

  .. _method-tilefilth-right:

  \ **uint8**\  *right*\ ()

  .. _method-tilefilth-right-2:

  \ **void**\  *right*\ (\ **uint8**\  _right)

class camera
############
  .. _method-camera-camera_type:

  \ **string**\  *camera_type*\ ()

  .. _method-camera-script_camera:

  \ **bool**\  *script_camera*\ ()

    A flag to disable the normal camera behavior. Set this to true if you wish
    to manage the camera position and zoom entirely within the script. 

  .. _method-camera-script_camera-2:

  \ **void**\  *script_camera*\ (\ **bool**\  script_camera)

  .. _method-camera-puppet:

  \ **entity**\ @ *puppet*\ ()

    The entity the camera is following. 

  .. _method-camera-player:

  \ **int**\  *player*\ ()

    Get the player index for this camera. 

  .. _method-camera-controller_mode:

  \ **int**\  *controller_mode*\ ()

    The controller mode controls how raw game inputs are converted into
    intents. ispressed, posedge, negedge each convert the corresponding intent
    to match the corresponding key's state: whether it's currently pressed, was
    just pushed, or just released. fall_intent is always 0 with a non-standard
    controller_mode because there is no corresponding key bind.
    

  .. _method-camera-controller_mode-2:

  \ **void**\  *controller_mode*\ (\ **int**\  controller_mode)

  .. _method-camera-x:

  \ **float**\  *x*\ ()

    Camera center coordinates. 

  .. _method-camera-x-2:

  \ **void**\  *x*\ (\ **float**\  x)

  .. _method-camera-y:

  \ **float**\  *y*\ ()

  .. _method-camera-y-2:

  \ **void**\  *y*\ (\ **float**\  y)

  .. _method-camera-prev_x:

  \ **float**\  *prev_x*\ ()

    The prev x/y values are used to interpolate the camera position. If you
    don't want the camera to move between the new and old camera positions
    reset these values appropriately. This is not necessary if you use
    camera.reset(). 

  .. _method-camera-prev_x-2:

  \ **void**\  *prev_x*\ (\ **float**\  prev_x)

  .. _method-camera-prev_y:

  \ **float**\  *prev_y*\ ()

  .. _method-camera-prev_y-2:

  \ **void**\  *prev_y*\ (\ **float**\  prev_y)

  .. _method-camera-zoom:

  \ **float**\  *zoom*\ ()

    Deprecated, use screen height instead.

  .. _method-camera-zoom-2:

  \ **void**\  *zoom*\ (\ **float**\  zoom)

  .. _method-camera-screen_height:

  \ **float**\  *screen_height*\ ()

    Access the height of the camera in pixels. 

  .. _method-camera-screen_height-2:

  \ **void**\  *screen_height*\ (\ **float**\  screen_height)

  .. _method-camera-screen_width:

  \ **float**\  *screen_width*\ ()

    Access the width of the camera in pixels. 

  .. _method-camera-screen_width-2:

  \ **void**\  *screen_width*\ (\ **float**\  screen_width)

  .. _method-camera-editor_zoom:

  \ **float**\  *editor_zoom*\ ()

    Access editor zoom setting.  

  .. _method-camera-editor_zoom-2:

  \ **void**\  *editor_zoom*\ (\ **float**\  editor_zoom)

  .. _method-camera-get_layer_draw_rect:

  \ **void**\  *get_layer_draw_rect*\ (\ **float**\  sub_frame, \ **int**\  layer, \ **float**\  &out left, \ **float**\  &out top, \ **float**\  &out width, \ **float**\  &out height)

    Get the size of the world layer in the current frame at a given
    sub_frame position. This accounts for camera animations and should
    match the sizes used by the game. 

  .. _method-camera-rotation:

  \ **float**\  *rotation*\ ()

    The camera rotation in degrees. 

  .. _method-camera-rotation-2:

  \ **void**\  *rotation*\ (\ **float**\  rotation)

  .. _method-camera-rotation_prev:

  \ **float**\  *rotation_prev*\ ()

  .. _method-camera-rotation_prev-2:

  \ **void**\  *rotation_prev*\ (\ **float**\  rotation_prev)

  .. _method-camera-scale_x:

  \ **float**\  *scale_x*\ ()

    These do the same thing as zoom but allow you to manipulate each axis
    individually. Negative values are support for axis flips. 

  .. _method-camera-scale_x-2:

  \ **void**\  *scale_x*\ (\ **float**\  scale_x)

  .. _method-camera-scale_y:

  \ **float**\  *scale_y*\ ()

  .. _method-camera-scale_y-2:

  \ **void**\  *scale_y*\ (\ **float**\  scale_y)

  .. _method-camera-prev_scale_x:

  \ **float**\  *prev_scale_x*\ ()

  .. _method-camera-prev_scale_x-2:

  \ **void**\  *prev_scale_x*\ (\ **float**\  prev_scale_x)

  .. _method-camera-prev_scale_y:

  \ **float**\  *prev_scale_y*\ ()

  .. _method-camera-prev_scale_y-2:

  \ **void**\  *prev_scale_y*\ (\ **float**\  prev_scale_y)

  .. _method-camera-add_screen_shake:

  \ **void**\  *add_screen_shake*\ (\ **float**\  x, \ **float**\  y, \ **float**\  dir, \ **float**\  force)

    Add a screen shake. Only works if script_camera is false, otherwise you
    need to simulate your own screen shake. 

  .. _method-camera-get_fog:

  \ **fog_setting**\ @ *get_fog*\ ()

    Get the current camera fog colours. 

  .. _method-camera-change_fog:

  \ **void**\  *change_fog*\ (\ **fog_setting**\ @ fog, \ **float**\  fog_time)

    Change the fog colour. fog_time controls how long the transition time
    from the current fog colour to this updated colour should take measured
    in seconds. 

class collision
###############
  Represents a collision hitbox used throughout the game engine. Collisions are
  made up of a collision type, a hitbox, and an entity. Collisions are used
  (e.g. when you attack an area) by querying all collision hitboxes of a certain
  type that intersect with a query rectangle (see scene.get_entity_collision)
  and returning the entities associated with each intersecting collision.
  
  Most enemies have two collisions associated with them. The base collision is
  used to detect tile collisions and when the entity is clicked in the editor.
  The hit collision is used to detect when an enemy is attacked. 

  .. _method-collision-rectangle:

  \ **void**\  *rectangle*\ (\ **float**\  top, \ **float**\  bottom, \ **float**\  left, \ **float**\  right)

    Access the hitbox of the collisio. 

  .. _method-collision-rectangle-2:

  \ **void**\  *rectangle*\ (\ **rectangle**\ @ rect, \ **float**\  x_offset, \ **float**\  y_offset)

  .. _method-collision-rectangle-3:

  \ **rectangle**\ @ *rectangle*\ ()

  .. _method-collision-collision_type:

  \ **uint32**\  *collision_type*\ ()

    Access the collision type of this collision. See col_type for predefined
    types. New values may be used for custom purposes as well. 

  .. _method-collision-collision_type-2:

  \ **void**\  *collision_type*\ (\ **uint32**\  collision_type)

  .. _method-collision-remove:

  \ **void**\  *remove*\ ()

    Remove the collision from the scene. This collision will no longer be
    picked up by calls to get_entity_collision. 

  .. _method-collision-entity:

  \ **void**\  *entity*\ (\ **entity**\ @ e)

    Access the entity associated with this collision. 

  .. _method-collision-entity-2:

  \ **entity**\ @ *entity*\ ()

class audio
###########
  .. _method-audio-stop:

  \ **void**\  *stop*\ ()

  .. _method-audio-is_playing:

  \ **bool**\  *is_playing*\ ()

  .. _method-audio-volume:

  \ **float**\  *volume*\ ()

  .. _method-audio-volume-2:

  \ **void**\  *volume*\ (\ **float**\  volume)

  .. _method-audio-time_scale:

  \ **float**\  *time_scale*\ ()

  .. _method-audio-time_scale-2:

  \ **void**\  *time_scale*\ (\ **float**\  time_scale)

  .. _method-audio-set_position:

  \ **void**\  *set_position*\ (\ **float**\  x, \ **float**\  y)

  .. _method-audio-positional:

  \ **bool**\  *positional*\ ()

  .. _method-audio-positional-2:

  \ **void**\  *positional*\ (\ **bool**\  positional)

class entity
############
  .. _method-entity-is_same:

  \ **bool**\  *is_same*\ (\ **entity**\ @ obj)

    Returns true if the underlying entity objects point to the same object.
    This is to help deal with the issue of different entity handles pointing to
    the same entity object in the scene. 

  .. _method-entity-is_same-2:

  \ **bool**\  *is_same*\ (\ **controllable**\ @ obj)

  .. _method-entity-is_same-3:

  \ **bool**\  *is_same*\ (\ **dustman**\ @ obj)

  .. _method-entity-metadata:

  \ **message**\ @ *metadata*\ ()

  .. _method-entity-get_sprites:

  \ **sprites**\ @ *get_sprites*\ ()

    Returns the entities' sprite object. 

  .. _method-entity-set_sprites:

  \ **void**\  *set_sprites*\ (\ **sprites**\ @ obj)

  .. _method-entity-type_name:

  \ **string**\  *type_name*\ ()

    Returns the type name of the entity. This is the same string that can
    be passed to create_entity to make an object of the same type. 

  .. _method-entity-vars:

  \ **varstruct**\ @ *vars*\ ()

  .. _method-entity-as_entity:

  \ **entity**\ @ *as_entity*\ ()

    Recast this object as an entity. Unfortunately with the way the API types
    are setup a controllable object cannot be casted to an entity using
    the normal cast<T>() operator. 

  .. _method-entity-as_controllable:

  \ **controllable**\ @ *as_controllable*\ ()

    Attempt to recast this object as a controllable. Returns null if the
    entity is not a controllable. 

  .. _method-entity-as_dustman:

  \ **dustman**\ @ *as_dustman*\ ()

    Attempt to recast this object as a dustman object. Returns null if
    the entity is not a dustman object. 

  .. _method-entity-as_hitbox:

  \ **hitbox**\ @ *as_hitbox*\ ()

    Attempt to recast this object as a hitbox object. Returns null if
    the entity is not a hitbox object. 

  .. _method-entity-as_scripttrigger:

  \ **scripttrigger**\ @ *as_scripttrigger*\ ()

    Attempt to recast this object as a scripttrigger object. Returns null if
    the entity is not a scripttrigger object. 

  .. _method-entity-as_scriptenemy:

  \ **scriptenemy**\ @ *as_scriptenemy*\ ()

    Attempt to recast this object as a scriptenemy object. Returns null if
    the entity is not a scriptenemy object. 

  .. _method-entity-id:

  \ **uint**\  *id*\ ()

    Return the ID associated with this entity that can be used with the
    entity_by_id() function. Non-persistant entities (i.e. the player
    entities) will have an id of 0 and cannot be found with entity_by_id(). 

  .. _method-entity-destroyed:

  \ **bool**\  *destroyed*\ ()

    Has this entity been removed from the scene. 

  .. _method-entity-x:

  \ **float**\  *x*\ ()

    The position of the entity. For most entities the position is the bottom
    center of their collision rectangle. These functions will automatically
    adjust the base and hit collisions associated with this entity. 

  .. _method-entity-x-2:

  \ **void**\  *x*\ (\ **float**\  x)

  .. _method-entity-y:

  \ **float**\  *y*\ ()

  .. _method-entity-y-2:

  \ **void**\  *y*\ (\ **float**\  y)

  .. _method-entity-set_xy:

  \ **void**\  *set_xy*\ (\ **float**\  x, \ **float**\  y)

  .. _method-entity-rotation:

  \ **float**\  *rotation*\ ()

    The rotation of the entity in degrees. This should be in the interval
    [-180, 180]. 

  .. _method-entity-rotation-2:

  \ **void**\  *rotation*\ (\ **float**\  rot)

  .. _method-entity-layer:

  \ **int**\  *layer*\ ()

    The layer that the entity should be drawn in. 

  .. _method-entity-layer-2:

  \ **void**\  *layer*\ (\ **int**\  layer)

  .. _method-entity-face:

  \ **int**\  *face*\ ()

    The direction the entity is facing. Should be -1 for left or 1 for right.
    If this is a controllable entity and the attack state is not
    attack_type_idle (i.e. non-zero) then the controllable will temporarily
    be facing the direction given by attack_face() instead. 

  .. _method-entity-face-2:

  \ **void**\  *face*\ (\ **int**\  face)

  .. _method-entity-palette:

  \ **int**\  *palette*\ ()

    The palette of sprites to use. Typically this should just be set to 1 as
    most entities don't have alternative palettes for their animations. 

  .. _method-entity-palette-2:

  \ **void**\  *palette*\ (\ **int**\  palette)

  .. _method-entity-time_warp:

  \ **float**\  *time_warp*\ ()

    Changes the perceived game speed for the entity. 

  .. _method-entity-time_warp-2:

  \ **void**\  *time_warp*\ (\ **float**\  time_warp)

  .. _method-entity-base_collision:

  \ **collision**\ @ *base_collision*\ ()

    Returns the collision rectangle used to select the entity in the editor. 

  .. _method-entity-base_rectangle:

  \ **rectangle**\ @ *base_rectangle*\ ()

  .. _method-entity-base_rectangle-2:

  \ **void**\  *base_rectangle*\ (\ **float**\  top, \ **float**\  bottom, \ **float**\  left, \ **float**\  right)

  .. _method-entity-base_rectangle-3:

  \ **void**\  *base_rectangle*\ (\ **rectangle**\ @ rect)

  .. _method-entity-send_message:

  \ **void**\  *send_message*\ (\ **string**\  id, \ **message**\ @ msg)

    Send a message to the entity. Currently, scripttrigger and scriptenemy
    entities are the only entities that can do anything with the message. 

class controllable
##################
  Inherits: `entity <#class-entity>`_

  .. _method-controllable-reset:

  \ **void**\  *reset*\ ()

    Reset the entity state to its defaults. 

  .. _method-controllable-prev_x:

  \ **float**\  *prev_x*\ ()

    The prev x/y values are used to interpolate the entity position. 

  .. _method-controllable-prev_x-2:

  \ **void**\  *prev_x*\ (\ **float**\  prev_x)

  .. _method-controllable-prev_y:

  \ **float**\  *prev_y*\ ()

  .. _method-controllable-prev_y-2:

  \ **void**\  *prev_y*\ (\ **float**\  prev_y)

  .. _method-controllable-x_speed:

  \ **float**\  *x_speed*\ ()

    Returns the x/y component of the velocity measured in pixels per second. 

  .. _method-controllable-y_speed:

  \ **float**\  *y_speed*\ ()

  .. _method-controllable-set_speed_xy:

  \ **void**\  *set_speed_xy*\ (\ **float**\  x_speed, \ **float**\  y_speed)

    Sets the velocity using x/y components. 

  .. _method-controllable-speed:

  \ **float**\  *speed*\ ()

    Returns magnitude of the velocity. 

  .. _method-controllable-direction:

  \ **float**\  *direction*\ ()

    Returns the direction of the velocity vector. Right is 90, Left is -90,
    Up is 0, Down is -180 or 180. 

  .. _method-controllable-set_speed_direction:

  \ **void**\  *set_speed_direction*\ (\ **float**\  speed, \ **int**\  direction)

    Sets the velocity using polar components. 

  .. _method-controllable-collision_rect:

  \ **rectangle**\ @ *collision_rect*\ ()

    Returns a copy of the collision rectangle for the entity. 

  .. _method-controllable-hurt_rect:

  \ **rectangle**\ @ *hurt_rect*\ ()

    Returns a copy of the hurtbox rectangle for the entity. 

  .. _method-controllable-scale:

  \ **float**\  *scale*\ ()

    Access the scale of the entity. A scale of 2.0 means double the usual size.
    A scale of 0.5 means half the usual size. If 'animate' is true the scale
    changes will gradually take affect. 

  .. _method-controllable-scale-2:

  \ **void**\  *scale*\ (\ **float**\  scale)

  .. _method-controllable-scale-3:

  \ **void**\  *scale*\ (\ **float**\  scale, \ **bool**\  animate)

  .. _method-controllable-state:

  \ **int**\  *state*\ ()

    Returns the current state of the entity. See the 'state_types' enum at the
    end of this documentation for details on the different states names.
    The majorify of the states are only used by dustman. 

  .. _method-controllable-state-2:

  \ **void**\  *state*\ (\ **int**\  state)

  .. _method-controllable-sprite_index:

  \ **string**\  *sprite_index*\ ()

    The sprite name currently being rendered for this entity. 

  .. _method-controllable-sprite_index-2:

  \ **void**\  *sprite_index*\ (\ **string**\  spr_index)

  .. _method-controllable-attack_sprite_index:

  \ **string**\  *attack_sprite_index*\ ()

    The sprite name currently being rendered for this entity. 

  .. _method-controllable-attack_sprite_index-2:

  \ **void**\  *attack_sprite_index*\ (\ **string**\  attack_spr_index)

  .. _method-controllable-state_timer:

  \ **float**\  *state_timer*\ ()

    The state timer for this entity. This tracks where the entity is in
    the state animation. 

  .. _method-controllable-state_timer-2:

  \ **void**\  *state_timer*\ (\ **float**\  state_timer)

  .. _method-controllable-stun_timer:

  \ **float**\  *stun_timer*\ ()

    The stun timer for this entity. This counts down to 0 which ends the stun
    animation. 

  .. _method-controllable-stun_timer-2:

  \ **void**\  *stun_timer*\ (\ **float**\  stun_timer)

  .. _method-controllable-attack_state:

  \ **int**\  *attack_state*\ ()

    The attack state for this entity. See 'attack_types' at the bottom of this
    documentation for the attack state types. 

  .. _method-controllable-attack_state-2:

  \ **void**\  *attack_state*\ (\ **int**\  attack_state)

  .. _method-controllable-attack_timer:

  \ **float**\  *attack_timer*\ ()

    The timer that keeps track of how long the attack has been active. 

  .. _method-controllable-attack_timer-2:

  \ **void**\  *attack_timer*\ (\ **float**\  attack_timer)

  .. _method-controllable-attack_face:

  \ **int**\  *attack_face*\ ()

    The direction the controllable is facing while attack state is not
    attack_type_idle. 

  .. _method-controllable-attack_face-2:

  \ **void**\  *attack_face*\ (\ **int**\  attack_face)

  .. _method-controllable-x_intent:

  \ **int**\  *x_intent*\ ()

    Indicates what direction the entity wants to move in the x direction. -1
    for left, 0 for neutral, 1 for right. 

  .. _method-controllable-x_intent-2:

  \ **void**\  *x_intent*\ (\ **int**\  x_intent)

  .. _method-controllable-y_intent:

  \ **int**\  *y_intent*\ ()

    Indicates what direction the entity wants to move in the y direction. -1
    for up, 0 for neutral, 1 for down. 

  .. _method-controllable-y_intent-2:

  \ **void**\  *y_intent*\ (\ **int**\  y_intent)

  .. _method-controllable-taunt_intent:

  \ **int**\  *taunt_intent*\ ()

    0 indicates taunt not pressed. 1 indicates taunt is pressed. 2 indicates
    taunt is pressed and the intent has been used. 

  .. _method-controllable-taunt_intent-2:

  \ **void**\  *taunt_intent*\ (\ **int**\  taunt_intent)

  .. _method-controllable-heavy_intent:

  \ **int**\  *heavy_intent*\ ()

    0 indicates no heavy intended. 10 indicates heavy pressed. When heavy is
    released and the intent was never used it counts down from 10 to 0 until
    the intent ends up being used or it hits 0. 11 indicates heavy is pressed
    and the intent has been used. 

  .. _method-controllable-heavy_intent-2:

  \ **void**\  *heavy_intent*\ (\ **int**\  heavy_intent)

  .. _method-controllable-light_intent:

  \ **int**\  *light_intent*\ ()

    Functions the same as heavy_intent() 

  .. _method-controllable-light_intent-2:

  \ **void**\  *light_intent*\ (\ **int**\  light_intent)

  .. _method-controllable-dash_intent:

  \ **int**\  *dash_intent*\ ()

    0 indicates no dash key press. 1 indicates the dash key pushed this frame.
    2 indicates the dash key pushed this frame and the intent has been used. 

  .. _method-controllable-dash_intent-2:

  \ **void**\  *dash_intent*\ (\ **int**\  dash_intent)

  .. _method-controllable-jump_intent:

  \ **int**\  *jump_intent*\ ()

    Same as taunt_intent() 

  .. _method-controllable-jump_intent-2:

  \ **void**\  *jump_intent*\ (\ **int**\  jump_intent)

  .. _method-controllable-fall_intent:

  \ **int**\  *fall_intent*\ ()

    Same as dash_intent() 

  .. _method-controllable-fall_intent-2:

  \ **void**\  *fall_intent*\ (\ **int**\  fall_intent)

  .. _method-controllable-life_initial:

  \ **int**\  *life_initial*\ ()

    Gives the initial life associated with this entity. This also usually
    corresponds to how much dust the enemy contributes toward completion
    score calculations. 

  .. _method-controllable-life:

  \ **int**\  *life*\ ()

    Access the number of hits remaining on this enemy. Setting the life
    negative will not destroy the enemy until it is hit again. A few
    controllables don't make use of this field (e.g. hittable_apple). 

  .. _method-controllable-life-2:

  \ **void**\  *life*\ (\ **int**\  life)

  .. _method-controllable-hitbox:

  \ **hitbox**\ @ *hitbox*\ ()

    Returns the current hitbox controller for this entity. This may be null
    if the controllabe isn't attacking. The hitbox object associated with each
    controllable is recreated with each attack. 

  .. _method-controllable-on_hit_callback:

  \ **void**\  *on_hit_callback*\ (\ **callback_base**\ @ base_obj, \ **string**\  callback_method, \ **int**\  arg)

    Set a callback when the entity is hit. The callback should have the
    signature "void func_name(controllable@ attacker, controllable@ attacked,
    hitbox@ attack_hitbox, int arg)". The 'arg' value passed to on_hit_callback
    will match the 'arg' parameter passed to the callback. 

  .. _method-controllable-on_hurt_callback:

  \ **void**\  *on_hurt_callback*\ (\ **callback_base**\ @ base_obj, \ **string**\  callback_method, \ **int**\  arg)

    Set a callback when the entity is hurt. The callback should have the
    signature "void func_name(controllable@ attacked, controllable@ attacker,
    hitbox@ attack_hitbox, int arg)". The 'arg' value passed to
    on_hurt_callback will match the 'arg' parameter passed to the callback. 

  .. _method-controllable-ground:

  \ **bool**\  *ground*\ ()

    Returns true if the controllable is in contact with the corresponding
    surface type. 

  .. _method-controllable-ground-2:

  \ **void**\  *ground*\ (\ **bool**\  ground)

  .. _method-controllable-roof:

  \ **bool**\  *roof*\ ()

  .. _method-controllable-roof-2:

  \ **void**\  *roof*\ (\ **bool**\  roof)

  .. _method-controllable-wall_left:

  \ **bool**\  *wall_left*\ ()

  .. _method-controllable-wall_left-2:

  \ **void**\  *wall_left*\ (\ **bool**\  wall_left)

  .. _method-controllable-wall_right:

  \ **bool**\  *wall_right*\ ()

  .. _method-controllable-wall_right-2:

  \ **void**\  *wall_right*\ (\ **bool**\  wall_right)

  .. _method-controllable-ground_surface_angle:

  \ **int**\  *ground_surface_angle*\ ()

    If the corresponding surface flag is set then these fields contain the
    angle of the surface the entity is touching. 

  .. _method-controllable-roof_surface_angle:

  \ **int**\  *roof_surface_angle*\ ()

  .. _method-controllable-left_surface_angle:

  \ **int**\  *left_surface_angle*\ ()

  .. _method-controllable-right_surface_angle:

  \ **int**\  *right_surface_angle*\ ()

  .. _method-controllable-set_ground_angles:

  \ **void**\  *set_ground_angles*\ (\ **int**\  slope_min, \ **int**\  slope_max, \ **int**\  slant_min, \ **int**\  slant_max)

    Change which ground surface angles this entity considers slopes, or slants.
    Slopes default to 45, and slants to 26.
    Required to allow non-45 degress slope sliding and for the player sprite to
    automatically rotate to match the ground angle. 

  .. _method-controllable-set_roof_angles:

  \ **void**\  *set_roof_angles*\ (\ **int**\  slope_min, \ **int**\  slope_max, \ **int**\  slant_min, \ **int**\  slant_max)

    Change which roof surface angles this entity considers slopes, or slants.
    Slopes defaults to 135, and slants to 154.
    Required for the player sprite to automatically rotate to match the
    ceiling angle. 

  .. _method-controllable-set_wall_angles:

  \ **void**\  *set_wall_angles*\ (\ **int**\  slant_down_min, \ **int**\  slant_down_max, \ **int**\  slant_up_min, \ **int**\  slant_up_max)

    Change which wall surface angles this entity considers down and up facing
    slants.
    Down facing defaults to 116, and up facing to 64.
    Required or wall angles outside of the range
    slant_up_min < 90 < slant_down_max
    won't work, even if the custom collision handler returns a collision. 

  .. _method-controllable-check_collision:

  \ **bool**\  *check_collision*\ (\ **tilecollision**\ @ t, \ **int**\  side, \ **bool**\  moving, \ **float**\  snap_offset)

    Performs the default collision check on the specified side used by
    all entities and writes the result into t.
    
    `moving` indicates if the collision should compensate for movement of
    the hitbox over the previous subframe (i.e. for checking for collisions
    between subframes).
    
    `snap_offset` indicates an additional offset outside of the collision
    for the entity to look for a surface used in e.g. wall snap jumps/dashes.
    
    Returns true if the collision hits anything.
    

  .. _method-controllable-set_collision_handler:

  \ **void**\  *set_collision_handler*\ (\ **callback_base**\ @ base_obj, \ **string**\  callback_method, \ **int**\  arg)

    Overrides the default tile collision checking for this entity.
    Setting `base_obj` to null will clear the handler.
    
    Arguments:
      :base_obj: The object the callback will be invoked on.
    
      :callback_method: The name of the function to invoke.
      :arg: An opaque value to be passed back to the callback when invoked.
    
    The callback should have the signature: ::
    
      void func_name(controllable@ ec, tilecollision@ tc, int side, bool moving, float snap_offset, int arg)
    
    Callback Arguments:
      :ec: The entity to check collisions for
      :tc: The tile collision object to write results to
      :side: which surface type to check for collisions, see the `side_types` enum.
      :moving: Indicates if the collision should compensate for movement over the last subframe.
      :snap_offset: Indicates an extra offset to look for collisions used in e.g. snap jumps/dashes
      :arg: The same value that was passed when registering the callback.
    
    Use the provided tilecollision object to return the results of the custom
    collision.
    
    Collision Results:
      :hit(): Set to true to indicate a collision happened
      :type(): Sets the surface angle of the collision (angle() is not used)
      :hit_x/y(): The position of the collision
    
    Calling :ref:`controllable::check_collision<method-controllable-check_collision>` can be used to
    perform the default tile collision handling when needed.
    

  .. _method-controllable-set_texture_type_handler:

  \ **void**\  *set_texture_type_handler*\ (\ **callback_base**\ @ base_obj, \ **string**\  callback_method, \ **int**\  arg)

    Overrides the default surface texture type lookup for entity.
    Setting base_obj to null will clear the handler.
    
    The callback should have the signature:
    void func_name(controllable@, texture_type_query@, int)
    
    See texture_type_query for details.
    

  .. _method-controllable-hit_collision:

  \ **collision**\ @ *hit_collision*\ ()

    Returns the hurt collision object for this controlable. 

  .. _method-controllable-hit_rectangle:

  \ **rectangle**\ @ *hit_rectangle*\ ()

  .. _method-controllable-hit_rectangle-2:

  \ **void**\  *hit_rectangle*\ (\ **float**\  top, \ **float**\  bottom, \ **float**\  left, \ **float**\  right)

  .. _method-controllable-hit_rectangle-3:

  \ **void**\  *hit_rectangle*\ (\ **rectangle**\ @ rect)

  .. _method-controllable-team:

  \ **int**\  *team*\ ()

    Access the team of the controllable. See the team_types enum for predefined
    values. Normally entities will only hit/target entities of the opposite
    team. 

  .. _method-controllable-team-2:

  \ **void**\  *team*\ (\ **int**\  team)

  .. _method-controllable-stun:

  \ **void**\  *stun*\ (\ **float**\  stun_x_speed, \ **float**\  stun_y_speed)

    Stuns the controllable. This does not break combo. 

  .. _method-controllable-freeze_frame_timer:

  \ **float**\  *freeze_frame_timer*\ ()

    Access the freeze frame timer for this entity. This timer usually runs
    at 24 units/s. 

  .. _method-controllable-freeze_frame_timer-2:

  \ **void**\  *freeze_frame_timer*\ (\ **float**\  freeze_frame_timer)

  .. _method-controllable-draw_offset_x:

  \ **float**\  *draw_offset_x*\ ()

    The game offsets the rendering of the sprites when on some surfaces or
    when stunned (and perhaps more). Added draw_offset_x() and draw_offset_y()
    to the entity's actual coordinates if you wish to compensate for this. Note
    that stun offsets are RNG and shouldn't affect game play.
    

  .. _method-controllable-draw_offset_y:

  \ **float**\  *draw_offset_y*\ ()

  .. _method-controllable-draw_offset_x-2:

  \ **void**\  *draw_offset_x*\ (\ **float**\  x_offset)

    Set the drawing offsets. This does not include stun offsets.
    

  .. _method-controllable-draw_offset_y-2:

  \ **void**\  *draw_offset_y*\ (\ **float**\  y_offset)

  .. _method-controllable-player_index:

  \ **int**\  *player_index*\ ()

    Return the player index of this controllable entity. If the entity is not
    associated with a player returns -1. This is the reverse function of
    controller_entity(player). 

class dustman
#############
  Inherits: `controllable <#class-controllable>`_

  .. _method-dustman-run_max:

  \ **float**\  *run_max*\ ()

  .. _method-dustman-run_max-2:

  \ **void**\  *run_max*\ (\ **float**\  run_max)

  .. _method-dustman-run_start:

  \ **float**\  *run_start*\ ()

  .. _method-dustman-run_start-2:

  \ **void**\  *run_start*\ (\ **float**\  run_start)

  .. _method-dustman-run_accel:

  \ **float**\  *run_accel*\ ()

  .. _method-dustman-run_accel-2:

  \ **void**\  *run_accel*\ (\ **float**\  run_accel)

  .. _method-dustman-run_accel_over:

  \ **float**\  *run_accel_over*\ ()

  .. _method-dustman-run_accel_over-2:

  \ **void**\  *run_accel_over*\ (\ **float**\  run_accel_over)

  .. _method-dustman-dash_speed:

  \ **float**\  *dash_speed*\ ()

  .. _method-dustman-dash_speed-2:

  \ **void**\  *dash_speed*\ (\ **float**\  dash_speed)

  .. _method-dustman-slope_slide_speed:

  \ **float**\  *slope_slide_speed*\ ()

  .. _method-dustman-slope_slide_speed-2:

  \ **void**\  *slope_slide_speed*\ (\ **float**\  slope_slide_speed)

  .. _method-dustman-slope_max:

  \ **float**\  *slope_max*\ ()

  .. _method-dustman-slope_max-2:

  \ **void**\  *slope_max*\ (\ **float**\  slope_max)

  .. _method-dustman-idle_fric:

  \ **float**\  *idle_fric*\ ()

  .. _method-dustman-idle_fric-2:

  \ **void**\  *idle_fric*\ (\ **float**\  idle_fric)

  .. _method-dustman-skid_fric:

  \ **float**\  *skid_fric*\ ()

  .. _method-dustman-skid_fric-2:

  \ **void**\  *skid_fric*\ (\ **float**\  skid_fric)

  .. _method-dustman-land_fric:

  \ **float**\  *land_fric*\ ()

  .. _method-dustman-land_fric-2:

  \ **void**\  *land_fric*\ (\ **float**\  land_fric)

  .. _method-dustman-roof_fric:

  \ **float**\  *roof_fric*\ ()

  .. _method-dustman-roof_fric-2:

  \ **void**\  *roof_fric*\ (\ **float**\  roof_fric)

  .. _method-dustman-skid_threshold:

  \ **float**\  *skid_threshold*\ ()

  .. _method-dustman-skid_threshold-2:

  \ **void**\  *skid_threshold*\ (\ **float**\  skid_threshold)

  .. _method-dustman-jump_a:

  \ **float**\  *jump_a*\ ()

  .. _method-dustman-jump_a-2:

  \ **void**\  *jump_a*\ (\ **float**\  jump_a)

  .. _method-dustman-hop_a:

  \ **float**\  *hop_a*\ ()

  .. _method-dustman-hop_a-2:

  \ **void**\  *hop_a*\ (\ **float**\  hop_a)

  .. _method-dustman-fall_max:

  \ **float**\  *fall_max*\ ()

  .. _method-dustman-fall_max-2:

  \ **void**\  *fall_max*\ (\ **float**\  fall_max)

  .. _method-dustman-fall_accel:

  \ **float**\  *fall_accel*\ ()

  .. _method-dustman-fall_accel-2:

  \ **void**\  *fall_accel*\ (\ **float**\  fall_accel)

  .. _method-dustman-hover_accel:

  \ **float**\  *hover_accel*\ ()

  .. _method-dustman-hover_accel-2:

  \ **void**\  *hover_accel*\ (\ **float**\  hover_accel)

  .. _method-dustman-heavy_fall_threshold:

  \ **float**\  *heavy_fall_threshold*\ ()

  .. _method-dustman-heavy_fall_threshold-2:

  \ **void**\  *heavy_fall_threshold*\ (\ **float**\  heavy_fall_threshold)

  .. _method-dustman-hover_fall_threshold:

  \ **float**\  *hover_fall_threshold*\ ()

  .. _method-dustman-hover_fall_threshold-2:

  \ **void**\  *hover_fall_threshold*\ (\ **float**\  hover_fall_threshold)

  .. _method-dustman-hitrise_speed:

  \ **float**\  *hitrise_speed*\ ()

  .. _method-dustman-hitrise_speed-2:

  \ **void**\  *hitrise_speed*\ (\ **float**\  hitrise_speed)

  .. _method-dustman-di_speed:

  \ **float**\  *di_speed*\ ()

  .. _method-dustman-di_speed-2:

  \ **void**\  *di_speed*\ (\ **float**\  di_speed)

  .. _method-dustman-di_speed_wall_lock:

  \ **float**\  *di_speed_wall_lock*\ ()

  .. _method-dustman-di_speed_wall_lock-2:

  \ **void**\  *di_speed_wall_lock*\ (\ **float**\  di_speed_wall_lock)

  .. _method-dustman-di_move_max:

  \ **float**\  *di_move_max*\ ()

  .. _method-dustman-di_move_max-2:

  \ **void**\  *di_move_max*\ (\ **float**\  di_move_max)

  .. _method-dustman-wall_slide_speed:

  \ **float**\  *wall_slide_speed*\ ()

  .. _method-dustman-wall_slide_speed-2:

  \ **void**\  *wall_slide_speed*\ (\ **float**\  wall_slide_speed)

  .. _method-dustman-wall_run_length:

  \ **float**\  *wall_run_length*\ ()

  .. _method-dustman-wall_run_length-2:

  \ **void**\  *wall_run_length*\ (\ **float**\  wall_run_length)

  .. _method-dustman-roof_run_length:

  \ **float**\  *roof_run_length*\ ()

  .. _method-dustman-roof_run_length-2:

  \ **void**\  *roof_run_length*\ (\ **float**\  roof_run_length)

  .. _method-dustman-attack_force_light:

  \ **float**\  *attack_force_light*\ ()

  .. _method-dustman-attack_force_light-2:

  \ **void**\  *attack_force_light*\ (\ **float**\  attack_force_light)

  .. _method-dustman-combo_count:

  \ **int**\  *combo_count*\ ()

  .. _method-dustman-combo_count-2:

  \ **void**\  *combo_count*\ (\ **int**\  combo_count)

  .. _method-dustman-skill_combo:

  \ **int**\  *skill_combo*\ ()

  .. _method-dustman-skill_combo-2:

  \ **void**\  *skill_combo*\ (\ **int**\  skill_combo)

  .. _method-dustman-skill_combo_max:

  \ **int**\  *skill_combo_max*\ ()

  .. _method-dustman-skill_combo_max-2:

  \ **void**\  *skill_combo_max*\ (\ **int**\  skill_combo_max)

  .. _method-dustman-combo_timer:

  \ **float**\  *combo_timer*\ ()

  .. _method-dustman-combo_timer-2:

  \ **void**\  *combo_timer*\ (\ **float**\  combo_timer)

  .. _method-dustman-total_filth:

  \ **int**\  *total_filth*\ ()

  .. _method-dustman-dash:

  \ **int**\  *dash*\ ()

    Query/set the number of air charges the player has. 

  .. _method-dustman-dash-2:

  \ **void**\  *dash*\ (\ **int**\  dash)

  .. _method-dustman-dash_max:

  \ **int**\  *dash_max*\ ()

    Query/set the maximum number of air charges the player has. 

  .. _method-dustman-dash_max-2:

  \ **void**\  *dash_max*\ (\ **int**\  dash_max)

  .. _method-dustman-character:

  \ **string**\  *character*\ ()

    Should be one of dustman, dustgirl, dustkid, dustworth, dustwraith,
    leafsprite, trashking, slimeboss. Optionally add 'v' to the start of the
    name to make it a virtual character. Using the string "default" will return
    the character choice to what the player initially selected. 

  .. _method-dustman-character-2:

  \ **void**\  *character*\ (\ **string**\  character)

  .. _method-dustman-ai_disabled:

  \ **bool**\  *ai_disabled*\ ()

    Normally dustman entities that aren't attached to a camera are taken over
    by the default AI implementation. Set this flag to disable this behavior.
    

  .. _method-dustman-ai_disabled-2:

  \ **void**\  *ai_disabled*\ (\ **bool**\  ai_disabled)

  .. _method-dustman-dead:

  \ **bool**\  *dead*\ ()

    Determines if the player is considered 'dead'. This is useful if you
    disable auto respawning or want to make the player invincible. 

  .. _method-dustman-dead-2:

  \ **void**\  *dead*\ (\ **bool**\  dead)

  .. _method-dustman-auto_respawn:

  \ **bool**\  *auto_respawn*\ ()

    Disable the player from respawning on death automatically. 

  .. _method-dustman-auto_respawn-2:

  \ **void**\  *auto_respawn*\ (\ **bool**\  auto_respawn)

  .. _method-dustman-kill:

  \ **void**\  *kill*\ (\ **bool**\  as_spikes)

    Simulate the player hitting a death zone if as_spikes=false, otherwise
    simulate them hitting spikes. Sets the dead flag but doesn't check if it
    was already set. 

  .. _method-dustman-on_subframe_end_callback:

  \ **void**\  *on_subframe_end_callback*\ (\ **callback_base**\ @ base_obj, \ **string**\  callback_method, \ **int**\  arg)

    Set a callback after every substep of this dustman object.
    The callback should have the
    signature "void func_name(dustman@ dm, int arg).
    The 'arg' value passed to on_subframe_end_callback
    will match the 'arg' parameter passed to the callback. 

class hitbox
############
  Inherits: `entity <#class-entity>`_

  .. _method-hitbox-owner:

  \ **controllable**\ @ *owner*\ ()

  .. _method-hitbox-damage:

  \ **int**\  *damage*\ ()

  .. _method-hitbox-damage-2:

  \ **void**\  *damage*\ (\ **int**\  damage)

  .. _method-hitbox-filth_type:

  \ **int**\  *filth_type*\ ()

  .. _method-hitbox-filth_type-2:

  \ **void**\  *filth_type*\ (\ **int**\  filth_type)

  .. _method-hitbox-aoe:

  \ **bool**\  *aoe*\ ()

    Used to indicate that the force from this hitbox should be applied radially
    outward from the center rather than using the attack_dir. 

  .. _method-hitbox-aoe-2:

  \ **void**\  *aoe*\ (\ **bool**\  aoe)

  .. _method-hitbox-state_timer:

  \ **float**\  *state_timer*\ ()

  .. _method-hitbox-state_timer-2:

  \ **void**\  *state_timer*\ (\ **float**\  state_timer)

  .. _method-hitbox-activate_time:

  \ **float**\  *activate_time*\ ()

  .. _method-hitbox-activate_time-2:

  \ **void**\  *activate_time*\ (\ **float**\  activate_time)

  .. _method-hitbox-timer_speed:

  \ **float**\  *timer_speed*\ ()

  .. _method-hitbox-timer_speed-2:

  \ **void**\  *timer_speed*\ (\ **float**\  timer_speed)

  .. _method-hitbox-attack_ff_strength:

  \ **float**\  *attack_ff_strength*\ ()

    Attack freeze frame strength. Controls how long the hit entity is frozen.
    

  .. _method-hitbox-attack_ff_strength-2:

  \ **void**\  *attack_ff_strength*\ (\ **float**\  attack_ff_strength)

  .. _method-hitbox-parry_ff_strength:

  \ **float**\  *parry_ff_strength*\ ()

  .. _method-hitbox-parry_ff_strength-2:

  \ **void**\  *parry_ff_strength*\ (\ **float**\  parry_ff_strength)

  .. _method-hitbox-stun_time:

  \ **float**\  *stun_time*\ ()

  .. _method-hitbox-stun_time-2:

  \ **void**\  *stun_time*\ (\ **float**\  stun_time)

  .. _method-hitbox-can_parry:

  \ **bool**\  *can_parry*\ ()

  .. _method-hitbox-can_parry-2:

  \ **void**\  *can_parry*\ (\ **bool**\  can_parry)

  .. _method-hitbox-attack_dir:

  \ **int**\  *attack_dir*\ ()

  .. _method-hitbox-attack_dir-2:

  \ **void**\  *attack_dir*\ (\ **int**\  attack_dir)

  .. _method-hitbox-attack_strength:

  \ **float**\  *attack_strength*\ ()

  .. _method-hitbox-attack_strength-2:

  \ **void**\  *attack_strength*\ (\ **float**\  attack_strength)

  .. _method-hitbox-team:

  \ **int**\  *team*\ ()

  .. _method-hitbox-team-2:

  \ **void**\  *team*\ (\ **int**\  team)

  .. _method-hitbox-attack_effect:

  \ **string**\  *attack_effect*\ ()

  .. _method-hitbox-attack_effect-2:

  \ **void**\  *attack_effect*\ (\ **string**\  attack_effect)

  .. _method-hitbox-effect_frame_rate:

  \ **int**\  *effect_frame_rate*\ ()

  .. _method-hitbox-effect_frame_rate-2:

  \ **void**\  *effect_frame_rate*\ (\ **int**\  effect_frame_rate)

  .. _method-hitbox-triggered:

  \ **bool**\  *triggered*\ ()

  .. _method-hitbox-hit_outcome:

  \ **int**\  *hit_outcome*\ ()

    See the hit_outcomes enumeration for possible values. 

class scripttrigger
###################
  Inherits: `entity <#class-entity>`_

  Represents a generic script-backed trigger. 

  .. _method-scripttrigger-get_object:

  \ **trigger_base**\ @ *get_object*\ ()

    Returns the script object backing this trigger. If this object is from a
    different script than the calling script this will return null instead. 

  .. _method-scripttrigger-script_name:

  \ **string**\  *script_name*\ ()

    Returns the name of the script this trigger comes from. 

  .. _method-scripttrigger-type_name:

  \ **string**\  *type_name*\ ()

    Returns the class name of this trigger within its script. 

  .. _method-scripttrigger-editor_selected:

  \ **bool**\  *editor_selected*\ ()

  .. _method-scripttrigger-radius:

  \ **int**\  *radius*\ ()

    Access the radius of the activation circle or square around this trigger.
    If the trigger has a square shape then the square extends width() out in
    each direction from the center of the trigger, i.e. it's side length is
    2*width(). 

  .. _method-scripttrigger-radius-2:

  \ **void**\  *radius*\ (\ **int**\  radius)

  .. _method-scripttrigger-square:

  \ **bool**\  *square*\ ()

    Access if the trigger has a square or circle activation area. 

  .. _method-scripttrigger-square-2:

  \ **void**\  *square*\ (\ **bool**\  square)

  .. _method-scripttrigger-editor_show_radius:

  \ **bool**\  *editor_show_radius*\ ()

    Access whether the radius is visible in the editor or not. 

  .. _method-scripttrigger-editor_show_radius-2:

  \ **void**\  *editor_show_radius*\ (\ **bool**\  show_radius)

  .. _method-scripttrigger-editor_handle_size:

  \ **int**\  *editor_handle_size*\ ()

    Access the size of the trigger handle in the editor. The handle size is how
    many pixels in each direction the handle should extend, default is 10. 

  .. _method-scripttrigger-editor_handle_size-2:

  \ **void**\  *editor_handle_size*\ (\ **int**\  handle_size)

  .. _method-scripttrigger-editor_colour_active:

  \ **uint**\  *editor_colour_active*\ ()

    Access the colour of the trigger handle when it is selected. 

  .. _method-scripttrigger-editor_colour_active-2:

  \ **void**\  *editor_colour_active*\ (\ **uint**\  colour)

  .. _method-scripttrigger-editor_colour_inactive:

  \ **uint**\  *editor_colour_inactive*\ ()

    Access the colour of the trigger handle when it is not selected. 

  .. _method-scripttrigger-editor_colour_inactive-2:

  \ **void**\  *editor_colour_inactive*\ (\ **uint**\  colour)

  .. _method-scripttrigger-editor_colour_circle:

  \ **uint**\  *editor_colour_circle*\ ()

    Access the colour of the activation circle/square. 

  .. _method-scripttrigger-editor_colour_circle-2:

  \ **void**\  *editor_colour_circle*\ (\ **uint**\  colour)

  .. _method-scripttrigger-editor_sync_vars_menu:

  \ **void**\  *editor_sync_vars_menu*\ ()

    Use after changing persistent variables via script to update values in the trigger script panel. 

class scriptenemy
#################
  Inherits: `controllable <#class-controllable>`_

  Represents a generic script-backed enemy. 

  .. _method-scriptenemy-get_object:

  \ **enemy_base**\ @ *get_object*\ ()

    Returns the enemy object backing this enemy. If this object is from a
    different script than the calling script this will return null instead. 

  .. _method-scriptenemy-script_name:

  \ **string**\  *script_name*\ ()

    Returns the name of the script this enemy comes from. 

  .. _method-scriptenemy-type_name:

  \ **string**\  *type_name*\ ()

    Returns the class name of this enemy within its script. 

  .. _method-scriptenemy-auto_physics:

  \ **bool**\  *auto_physics*\ ()

  .. _method-scriptenemy-auto_physics-2:

  \ **void**\  *auto_physics*\ (\ **bool**\  auto_physics)

  .. _method-scriptenemy-editor_sync_vars_menu:

  \ **void**\  *editor_sync_vars_menu*\ ()

    Use after changing persistent variables via script to update values in the enemy script panel. 

class sprites
#############
  Represents a set of sprites that can be drawn. Sprites are organized into
  sprite set files that can be seen in 'content/sprites' and can be added
  into this sprite object using 'add_sprite_set' call.
  
  Each sprite set file has a list of sprite names. These names can be
  enumerated using get_sprite_count(sprite_set) and
  get_sprite_name(sprite_set, i).
  
  Each sprite name has some number of color palettes (most often it's just 1)
  which can be counted using get_palette_count(). They also have
  some number of frames which you can calculate with get_animation_length().
  
  You can download all of the sprites from
  https://www.dropbox.com/s/11pa1cdqhv68etv/sprites.rar?dl=0 although the
  folder structure doesn't always match the sprite set structure used in game.
  

  .. _method-sprites-add_sprite_set:

  \ **void**\  *add_sprite_set*\ (\ **string**\  sprite_set)

    Add a sprite set's sprites into this sprites object. After this call we can
    refer to any contained sprites with
    draw/get_palette_count/get_animation_length.  Any duplicate sprite
    names will be overwritten to point to the most recently added sprite set.
    

  .. _method-sprites-get_animation_length:

  \ **int**\  *get_animation_length*\ (\ **string**\  sprite_name)

    Returns the number of frames the named sprite last. 

  .. _method-sprites-get_palette_count:

  \ **uint**\  *get_palette_count*\ (\ **string**\  sprite_name)

    Returns the number of palettes associated with the sprite. Tile sprites are
    typically the only sprites to have multiple palettes. 

  .. _method-sprites-get_sprite_count:

  \ **uint**\  *get_sprite_count*\ (\ **string**\  sprite_set)

    Returns the number of sprites contained in the sprite set. 

  .. _method-sprites-get_sprite_name:

  \ **string**\  *get_sprite_name*\ (\ **string**\  sprite_set, \ **uint**\  index)

    Returns the name of the index'th sprite in sprite_set. 

  .. _method-sprites-get_sprite_rect:

  \ **rectangle**\ @ *get_sprite_rect*\ (\ **string**\  sprite_name, \ **uint32**\  frame)

    Returns the bounding rectangle around the sprite if it were rendered at the
    origin. 

  .. _method-sprites-draw_world:

  \ **void**\  *draw_world*\ (\ **int**\  layer, \ **int**\  sub_layer, \ **string**\  spriteName, \ **uint32**\  frame, \ **uint32**\  palette, \ **float**\  x, \ **float**\  y, \ **float**\  rotation, \ **float**\  scale_x, \ **float**\  scale_y, \ **uint32**\  colour)

    Draw a sprite to the world.
    1 <= palette <= get_palette_count(spriteName)
    0 <= frame < get_animation_length(spriteName)
    
    colour is an ARGB colour vector that is multiplied with the actual color
    values rendered. This does not include color manipulation through fog
    colours. Setting colour to 0xFFFFFFFF draws the sprite normally with only
    fog colour applied.
    

  .. _method-sprites-draw_hud:

  \ **void**\  *draw_hud*\ (\ **int**\  layer, \ **int**\  sub_layer, \ **string**\  spriteName, \ **uint32**\  frame, \ **uint32**\  palette, \ **float**\  x, \ **float**\  y, \ **float**\  rotation, \ **float**\  scale_x, \ **float**\  scale_y, \ **uint32**\  colour)

    Like draw_world except drawing in the hud. 

class prop
##########
  .. _method-prop-id:

  \ **uint**\  *id*\ ()

    Return the ID associated with this prop that can be used with the
    prop_by_id() function. All props that have been added to the scene should
    have an ID. 

  .. _method-prop-x:

  \ **float**\  *x*\ ()

  .. _method-prop-x-2:

  \ **void**\  *x*\ (\ **float**\  x)

  .. _method-prop-y:

  \ **float**\  *y*\ ()

  .. _method-prop-y-2:

  \ **void**\  *y*\ (\ **float**\  y)

  .. _method-prop-rotation:

  \ **float**\  *rotation*\ ()

  .. _method-prop-rotation-2:

  \ **void**\  *rotation*\ (\ **float**\  rotation)

  .. _method-prop-scale_x:

  \ **float**\  *scale_x*\ ()

  .. _method-prop-scale_x-2:

  \ **void**\  *scale_x*\ (\ **float**\  scale_x)

  .. _method-prop-scale_y:

  \ **float**\  *scale_y*\ ()

  .. _method-prop-scale_y-2:

  \ **void**\  *scale_y*\ (\ **float**\  scale_y)

  .. _method-prop-prop_set:

  \ **uint**\  *prop_set*\ ()

    C has an excellent reference to find the prop set/group/index for props
    which can be found at
    https://github.com/cmann1/PropUtils/tree/master/files/prop_reference. The
    three numbers listed under each prop correspond to the set, group, and
    index for that prop. 

  .. _method-prop-prop_set-2:

  \ **void**\  *prop_set*\ (\ **uint**\  prop_set)

  .. _method-prop-prop_group:

  \ **uint**\  *prop_group*\ ()

  .. _method-prop-prop_group-2:

  \ **void**\  *prop_group*\ (\ **uint**\  prop_group)

  .. _method-prop-prop_index:

  \ **uint**\  *prop_index*\ ()

  .. _method-prop-prop_index-2:

  \ **void**\  *prop_index*\ (\ **uint**\  prop_index)

  .. _method-prop-palette:

  \ **uint**\  *palette*\ ()

    The palette for the prop. Most (all?) props only support palette 1. 

  .. _method-prop-palette-2:

  \ **void**\  *palette*\ (\ **uint**\  palette)

  .. _method-prop-layer:

  \ **uint**\  *layer*\ ()

    The layer to render the prop in. 

  .. _method-prop-layer-2:

  \ **void**\  *layer*\ (\ **uint**\  layer)

  .. _method-prop-sub_layer:

  \ **uint**\  *sub_layer*\ ()

    The sublayer to render the prop in. 

  .. _method-prop-sub_layer-2:

  \ **void**\  *sub_layer*\ (\ **uint**\  sub_layer)

class textfield
###############
  Represents a text field used to render text to the screen. 

  .. _method-textfield-text:

  \ **string**\  *text*\ ()

    Access the text to be rendered or measured. 

  .. _method-textfield-text-2:

  \ **void**\  *text*\ (\ **string**\  text)

  .. _method-textfield-font:

  \ **string**\  *font*\ ()

    Get and set the font used to render the text. See
    https://pastebin.com/YcNKSXd9 for a list of supported fonts and font
    sizes. 

  .. _method-textfield-font_size:

  \ **uint**\  *font_size*\ ()

  .. _method-textfield-set_font:

  \ **void**\  *set_font*\ (\ **string**\  font, \ **uint**\  font_size)

  .. _method-textfield-colour:

  \ **uint**\  *colour*\ ()

    Set the colour of the text as an ARGB value. 

  .. _method-textfield-colour-2:

  \ **void**\  *colour*\ (\ **uint**\  colour)

  .. _method-textfield-align_horizontal:

  \ **int**\  *align_horizontal*\ ()

    Set the horizontal alignment when drawing the text. -1 aligns the left of
    the text to the given x coordinate. 0 centers the text at the given x
    coordinate. 1 aligns the right of the text to the given x coordinate. 

  .. _method-textfield-align_horizontal-2:

  \ **void**\  *align_horizontal*\ (\ **int**\  align_h)

  .. _method-textfield-align_vertical:

  \ **int**\  *align_vertical*\ ()

    Set the vertical alignment when drawing the text. -1 aligns the top of the
    text to the given y coordinate.  0 centers the text at the given y
    coordinate. 1 aligns the bottom of the text to the given y coordinate.
    

  .. _method-textfield-align_vertical-2:

  \ **void**\  *align_vertical*\ (\ **int**\  align_v)

  .. _method-textfield-text_width:

  \ **int**\  *text_width*\ ()

    Measures the width of the text when drawn. 

  .. _method-textfield-text_height:

  \ **int**\  *text_height*\ ()

    Measures the height of the text when drawn. 

  .. _method-textfield-draw_world:

  \ **void**\  *draw_world*\ (\ **int**\  layer, \ **int**\  sub_layer, \ **float**\  x, \ **float**\  y, \ **float**\  scale_x, \ **float**\  scale_y, \ **float**\  rotation)

  .. _method-textfield-draw_hud:

  \ **void**\  *draw_hud*\ (\ **int**\  layer, \ **int**\  sub_layer, \ **float**\  x, \ **float**\  y, \ **float**\  scale_x, \ **float**\  scale_y, \ **float**\  rotation)

class varvalue
##############
  A common interface used to represent a variable of any type. 

  .. _method-varvalue-type_id:

  \ **int**\  *type_id*\ ()

    Returns the type of the variable.  See 'var_types' at the end of this
    documentation for details on the different types. 

  .. _method-varvalue-get_bool:

  \ **bool**\  *get_bool*\ ()

    Get or set the value. The getter or setter used must match the type_id() of
    the var. 

  .. _method-varvalue-set_bool:

  \ **void**\  *set_bool*\ (\ **bool**\  val)

  .. _method-varvalue-get_int8:

  \ **int8**\  *get_int8*\ ()

  .. _method-varvalue-set_int8:

  \ **void**\  *set_int8*\ (\ **int8**\  val)

  .. _method-varvalue-get_int16:

  \ **int16**\  *get_int16*\ ()

  .. _method-varvalue-set_int16:

  \ **void**\  *set_int16*\ (\ **int16**\  val)

  .. _method-varvalue-get_int32:

  \ **int32**\  *get_int32*\ ()

  .. _method-varvalue-set_int32:

  \ **void**\  *set_int32*\ (\ **int32**\  val)

  .. _method-varvalue-get_int64:

  \ **int64**\  *get_int64*\ ()

  .. _method-varvalue-set_int64:

  \ **void**\  *set_int64*\ (\ **int64**\  val)

  .. _method-varvalue-get_float:

  \ **float**\  *get_float*\ ()

  .. _method-varvalue-set_float:

  \ **void**\  *set_float*\ (\ **float**\  val)

  .. _method-varvalue-get_string:

  \ **string**\  *get_string*\ ()

  .. _method-varvalue-set_string:

  \ **void**\  *set_string*\ (\ **string**\  val)

  .. _method-varvalue-get_vec2_x:

  \ **float**\  *get_vec2_x*\ ()

  .. _method-varvalue-get_vec2_y:

  \ **float**\  *get_vec2_y*\ ()

  .. _method-varvalue-set_vec2:

  \ **void**\  *set_vec2*\ (\ **float**\  x, \ **float**\  y)

  .. _method-varvalue-get_struct:

  \ **varstruct**\ @ *get_struct*\ ()

    Returns a modifiable handle to the struct pointed to by this var. 

  .. _method-varvalue-get_array:

  \ **vararray**\ @ *get_array*\ ()

    Returns a modifiable handle to the array pointed to by this var. 

class vararray
##############
  Represents an array of variables. 

  .. _method-vararray-at:

  \ **varvalue**\ @ *at*\ (\ **uint32**\  index)

    Get the i-th value in this array. Returns null for indicies outside the
    bounds of the array. 

  .. _method-vararray-element_type_id:

  \ **int**\  *element_type_id*\ ()

    Returns the element type of this array. 

  .. _method-vararray-size:

  \ **uint32**\  *size*\ ()

    Returns the size of this array. 

  .. _method-vararray-resize:

  \ **void**\  *resize*\ (\ **uint32**\  size)

    Resizes this array. If the array size is extended the new elements are not
    initialized. 

class varstruct
###############
  Represents a dictionary of string keys to vars. 

  .. _method-varstruct-get_var:

  \ **varvalue**\ @ *get_var*\ (\ **string**\  var)

    Retrieves a var based on its name. 

  .. _method-varstruct-get_var-2:

  \ **varvalue**\ @ *get_var*\ (\ **uint32**\  index)

    Retrieves the index'th var. 

  .. _method-varstruct-num_vars:

  \ **uint32**\  *num_vars*\ ()

    Returns the number of vars in this struct. 

  .. _method-varstruct-type_name:

  \ **string**\  *type_name*\ ()

    Returns the type name of the struct. 

  .. _method-varstruct-var_name:

  \ **string**\  *var_name*\ (\ **uint32**\  index)

    Returns the name of the index'th var. 

class message
#############
  .. _method-message-get_int:

  \ **int**\  *get_int*\ (\ **string**\  key)

  .. _method-message-get_int-2:

  \ **int**\  *get_int*\ (\ **string**\  key, \ **int**\  def)

  .. _method-message-set_int:

  \ **void**\  *set_int*\ (\ **string**\  key, \ **int**\  val)

  .. _method-message-has_int:

  \ **bool**\  *has_int*\ (\ **string**\  key)

  .. _method-message-num_int:

  \ **uint**\  *num_int*\ ()

  .. _method-message-get_key_int:

  \ **string**\  *get_key_int*\ (\ **uint**\  index)

  .. _method-message-get_float:

  \ **float**\  *get_float*\ (\ **string**\  key)

  .. _method-message-get_float-2:

  \ **float**\  *get_float*\ (\ **string**\  key, \ **float**\  def)

  .. _method-message-set_float:

  \ **void**\  *set_float*\ (\ **string**\  key, \ **float**\  val)

  .. _method-message-has_float:

  \ **bool**\  *has_float*\ (\ **string**\  key)

  .. _method-message-num_float:

  \ **uint**\  *num_float*\ ()

  .. _method-message-get_key_float:

  \ **string**\  *get_key_float*\ (\ **uint**\  index)

  .. _method-message-get_string:

  \ **string**\  *get_string*\ (\ **string**\  key)

  .. _method-message-get_string-2:

  \ **string**\  *get_string*\ (\ **string**\  key, \ **string**\  def)

  .. _method-message-set_string:

  \ **void**\  *set_string*\ (\ **string**\  key, \ **string**\  val)

  .. _method-message-has_string:

  \ **bool**\  *has_string*\ (\ **string**\  key)

  .. _method-message-num_string:

  \ **uint**\  *num_string*\ ()

  .. _method-message-get_key_string:

  \ **string**\  *get_key_string*\ (\ **uint**\  index)

  .. _method-message-get_entity:

  \ **entity**\ @ *get_entity*\ (\ **string**\  key)

  .. _method-message-set_entity:

  \ **void**\  *set_entity*\ (\ **string**\  key, \ **entity**\ @ e)

  .. _method-message-has_entity:

  \ **bool**\  *has_entity*\ (\ **string**\  key)

  .. _method-message-num_entity:

  \ **uint**\  *num_entity*\ ()

  .. _method-message-get_key_entity:

  \ **string**\  *get_key_entity*\ (\ **uint**\  index)

class var_info
##############
  .. _method-var_info-get_name:

  \ **string**\  *get_name*\ ()

    Returns the name of the variable that changed 

  .. _method-var_info-get_index:

  \ **int**\  *get_index*\ ()

    Returns the index that was changed, or -1 if this variable is not an array 

  .. _method-var_info-get_path_length:

  \ **int**\  *get_path_length*\ ()

    For nested variables returns the number of variables above this one 

  .. _method-var_info-get_name-2:

  \ **string**\  *get_name*\ (\ **uint**\  index)

    Returns the name of the parent variable at the specified level 

  .. _method-var_info-get_index-2:

  \ **int**\  *get_index*\ (\ **uint**\  index)

    Returns the array index of the parent variable at the specified level, or -1 if it is not an array 

  .. _method-var_info-get_path:

  \ **string**\  *get_path*\ (\ **bool**\  include_array_indices)

    Convenience method that returns the entire path as a string
    in the format: "parent_var.parent_var2.var"
    If include_array_indices is true, arrays in the path will also
    include an index, e.g. "parent_var[i]" 

class texture_type_query
########################
  Certain sounds, e.g. player footstep sounds, check the tiles around the
  player's feet to determine which sounds to play based on the tile
  sprite set and index. controllable::set_texture_type_handler can be used
  to bypass that behaviour and provide a custom texture type.
  
  This class is used to pass values back and forth during a texture
  type callback registered with controllable::set_texture_type_handler.
  

  .. _method-texture_type_query-x:

  \ **int**\  *x*\ ()

    The location to check 

  .. _method-texture_type_query-y:

  \ **int**\  *y*\ ()

    The location to check 

  .. _method-texture_type_query-top_surface:

  \ **bool**\  *top_surface*\ ()

    Is the query for a ground surface? 

  .. _method-texture_type_query-result:

  \ **string**\  *result*\ ()

  .. _method-texture_type_query-result-2:

  \ **void**\  *result*\ (\ **string**\  result)

    Set this to return the texture type or use an empty string to
    use the default texture lookup.
    
    Valid textures are `"none"`, `"stone"`, `"dirt"`, `"metal"`, `"grass"`
    `"water"`, `"wood"`, `"carpet"`, or `"poly"`.
    

class canvas
############
  A configurable drawing surface that supports affine transformations.
  
  The transformaton matrix is stored in the form ::
  
    [x']   [m00 m01 ox] [x]
    [y'] = [m10 m11 oy] [y]
    [1 ]   [0   0   1 ] [1]
  

  .. _method-canvas-hud:

  \ **bool**\  *hud*\ ()

    Access whether this canvas draws to the hud or world. 

  .. _method-canvas-hud-2:

  \ **void**\  *hud*\ (\ **bool**\  hud)

  .. _method-canvas-layer:

  \ **int**\  *layer*\ ()

    Access what layer this canvas draws to. 

  .. _method-canvas-layer-2:

  \ **void**\  *layer*\ (\ **int**\  layer)

  .. _method-canvas-sub_layer:

  \ **int**\  *sub_layer*\ ()

    Access what sub layer this canvas draws to. 

  .. _method-canvas-sub_layer-2:

  \ **void**\  *sub_layer*\ (\ **int**\  sub_layer)

  .. _method-canvas-draw_rectangle:

  \ **void**\  *draw_rectangle*\ (\ **float**\  x1, \ **float**\  y1, \ **float**\  x2, \ **float**\  y2, \ **float**\  rotation, \ **uint**\  colour)

    These draw routines mirror the existing draw routines using the canvas
    specific options and transformation. 

  .. _method-canvas-draw_glass:

  \ **void**\  *draw_glass*\ (\ **float**\  x1, \ **float**\  y1, \ **float**\  x2, \ **float**\  y2, \ **float**\  rotation, \ **uint**\  colour)

  .. _method-canvas-draw_gradient:

  \ **void**\  *draw_gradient*\ (\ **float**\  x1, \ **float**\  y1, \ **float**\  x2, \ **float**\  y2, \ **uint**\  c00, \ **uint**\  c10, \ **uint**\  c11, \ **uint**\  c01)

  .. _method-canvas-draw_line:

  \ **void**\  *draw_line*\ (\ **float**\  x1, \ **float**\  y1, \ **float**\  x2, \ **float**\  y2, \ **float**\  width, \ **uint**\  colour)

  .. _method-canvas-draw_quad:

  \ **void**\  *draw_quad*\ (\ **bool**\  is_glass, \ **float**\  x1, \ **float**\  y1, \ **float**\  x2, \ **float**\  y2, \ **float**\  x3, \ **float**\  y3, \ **float**\  x4, \ **float**\  y4, \ **uint**\  c1, \ **uint**\  c2, \ **uint**\  c3, \ **uint**\  c4)

  .. _method-canvas-draw_sprite:

  \ **void**\  *draw_sprite*\ (\ **sprites**\ @ spr, \ **string**\  spriteName, \ **uint32**\  frame, \ **uint32**\  palette, \ **float**\  x, \ **float**\  y, \ **float**\  rotation, \ **float**\  scale_x, \ **float**\  scale_y, \ **uint32**\  colour)

  .. _method-canvas-text:

  \ **void**\  *text*\ (\ **draw**\ @ txt, \ **float**\  x, \ **float**\  y, \ **float**\  scale_x, \ **float**\  scale_y, \ **float**\  rotation)

  .. _method-canvas-draw_text:

  \ **void**\  *draw_text*\ (\ **textfield**\ @ txt, \ **float**\  x, \ **float**\  y, \ **float**\  scale_x, \ **float**\  scale_y, \ **float**\  rotation)

  .. _method-canvas-transform_point:

  \ **void**\  *transform_point*\ (\ **float**\  x, \ **float**\  y, \ **float**\  &out tx, \ **float**\  &out ty)

    Compute the x/y coordinates of the underlying canvas transform. 

  .. _method-canvas-multiply:

  \ **void**\  *multiply*\ (\ **float**\  m00, \ **float**\  m01, \ **float**\  m10, \ **float**\  m11, \ **float**\  ox, \ **float**\  oy)

    Right multiply a generic affine matrix. 

  .. _method-canvas-multiply_left:

  \ **void**\  *multiply_left*\ (\ **float**\  m00, \ **float**\  m01, \ **float**\  m10, \ **float**\  m11, \ **float**\  ox, \ **float**\  oy)

    Left multiply a generic affine matrix. 

  .. _method-canvas-scale:

  \ **void**\  *scale*\ (\ **float**\  scale_x, \ **float**\  scale_y)

    Each transformation option has a right (default) and left multiply variant.
    A right multiply transformation is applied to the source coordinates, a
    left multiply is applied to the transformed coordinates.
    

  .. _method-canvas-scale_left:

  \ **void**\  *scale_left*\ (\ **float**\  scale_x, \ **float**\  scale_y)

  .. _method-canvas-translate:

  \ **void**\  *translate*\ (\ **float**\  ox, \ **float**\  oy)

  .. _method-canvas-translate_left:

  \ **void**\  *translate_left*\ (\ **float**\  ox, \ **float**\  oy)

  .. _method-canvas-rotate:

  \ **void**\  *rotate*\ (\ **float**\  degrees, \ **float**\  center_x, \ **float**\  center_y)

  .. _method-canvas-rotate_left:

  \ **void**\  *rotate_left*\ (\ **float**\  degrees, \ **float**\  center_x, \ **float**\  center_y)

  .. _method-canvas-push:

  \ **void**\  *push*\ ()

    Push the current transform settings onto a stack. pop() can later be used
    to return these settings. Note that this only affects the transform
    settings of this canvas. 

  .. _method-canvas-pop:

  \ **void**\  *pop*\ ()

  .. _method-canvas-reset:

  \ **void**\  *reset*\ ()

    Reset the transform to the identity transform and clear the transform
    stack. 

  .. _method-canvas-scale_hud:

  \ **bool**\  *scale_hud*\ ()

    Control whether or not the coordinates should be auto-scaled to simulate a
    1600-900 sized screen. Only changes behavior for hud canvases. By default
    this is set to true.
    

  .. _method-canvas-scale_hud-2:

  \ **void**\  *scale_hud*\ (\ **bool**\  scale_hud)

class timedate
##############
  Definitions match those described in
  http://www.cplusplus.com/reference/ctime/tm/
  

  .. _method-timedate-sec:

  \ **int**\  *sec*\ ()

  .. _method-timedate-min:

  \ **int**\  *min*\ ()

  .. _method-timedate-hour:

  \ **int**\  *hour*\ ()

  .. _method-timedate-mday:

  \ **int**\  *mday*\ ()

  .. _method-timedate-mon:

  \ **int**\  *mon*\ ()

  .. _method-timedate-year:

  \ **int**\  *year*\ ()

  .. _method-timedate-wday:

  \ **int**\  *wday*\ ()

  .. _method-timedate-yday:

  \ **int**\  *yday*\ ()

  .. _method-timedate-isdst:

  \ **int**\  *isdst*\ ()

class fog_setting
#################
  .. _method-fog_setting-layer_index:

  \ **uint**\  *layer_index*\ (\ **uint**\  layer, \ **uint**\  sublayer)

  .. _method-fog_setting-colour:

  \ **uint**\  *colour*\ (\ **uint**\  layer, \ **uint**\  sublayer)

    Access the layer and sublayer fog colours. 

  .. _method-fog_setting-colour-2:

  \ **void**\  *colour*\ (\ **uint**\  layer, \ **uint**\  sublayer, \ **uint**\  colour)

  .. _method-fog_setting-layer_colour:

  \ **void**\  *layer_colour*\ (\ **uint**\  layer, \ **uint**\  colour)

  .. _method-fog_setting-percent:

  \ **float**\  *percent*\ (\ **uint**\  layer, \ **uint**\  sublayer)

    Access the layer and sublayer fog percents. The percent for each
    layer/sublayer indicates how to mix the fog colour with the graphics
    on that layer. A percent of 0 ignores the fog colour and a percent
    of 1 replaces all colours in drawn graphics with the fog colour. 

  .. _method-fog_setting-percent-2:

  \ **void**\  *percent*\ (\ **uint**\  layer, \ **uint**\  sublayer, \ **float**\  percent)

  .. _method-fog_setting-layer_percent:

  \ **void**\  *layer_percent*\ (\ **uint**\  layer, \ **float**\  percent)

  .. _method-fog_setting-bg_mid_point:

  \ **float**\  *bg_mid_point*\ ()

    Access where on the screen the screen the middle background colour
    is rendered. Should be between 0 and 1 with 0 indicating the top of
    the screen and 1 the bottom. 

  .. _method-fog_setting-bg_mid_point-2:

  \ **void**\  *bg_mid_point*\ (\ **float**\  bg_mid_point)

  .. _method-fog_setting-bg_top:

  \ **uint**\  *bg_top*\ ()

    Access the background colour at the top of the screen. 

  .. _method-fog_setting-bg_top-2:

  \ **void**\  *bg_top*\ (\ **uint**\  bg_top)

  .. _method-fog_setting-bg_mid:

  \ **uint**\  *bg_mid*\ ()

    Access the background colour in the middle of the screen. 

  .. _method-fog_setting-bg_mid-2:

  \ **void**\  *bg_mid*\ (\ **uint**\  bg_mid)

  .. _method-fog_setting-bg_bot:

  \ **uint**\  *bg_bot*\ ()

    Access the background colour at the bottom of the screen. 

  .. _method-fog_setting-bg_bot-2:

  \ **void**\  *bg_bot*\ (\ **uint**\  bg_bot)

  .. _method-fog_setting-stars_top:

  \ **float**\  *stars_top*\ ()

    Access the star saturation at the top of the screen. Should be
    a number between 0 and 1. 

  .. _method-fog_setting-stars_top-2:

  \ **void**\  *stars_top*\ (\ **float**\  s_top)

  .. _method-fog_setting-stars_mid:

  \ **float**\  *stars_mid*\ ()

    Access the star saturation in the middle of the screen. 

  .. _method-fog_setting-stars_mid-2:

  \ **void**\  *stars_mid*\ (\ **float**\  s_mid)

  .. _method-fog_setting-stars_bot:

  \ **float**\  *stars_bot*\ ()

    Access the star saturation at the bottom of the screen. 

  .. _method-fog_setting-stars_bot-2:

  \ **void**\  *stars_bot*\ (\ **float**\  s_bot)

class editor_api
################
  .. _method-editor_api-key_check_vk:

  \ **bool**\  *key_check_vk*\ (\ **int**\  vk)

    Deprecated. Use :ref:`class input_api` instead. 

  .. _method-editor_api-key_check_pressed_vk:

  \ **bool**\  *key_check_pressed_vk*\ (\ **int**\  vk)

    Deprecated. Use :ref:`class input_api` instead. 

  .. _method-editor_api-key_check_gvb:

  \ **bool**\  *key_check_gvb*\ (\ **int**\  gvb)

    Deprecated. Use :ref:`class input_api` instead. 

  .. _method-editor_api-key_check_pressed_gvb:

  \ **bool**\  *key_check_pressed_gvb*\ (\ **int**\  gvb)

    Deprecated. Use :ref:`class input_api` instead. 

  .. _method-editor_api-key_clear_gvb:

  \ **void**\  *key_clear_gvb*\ (\ **int**\  gvb)

    Deprecated. Use :ref:`class input_api` instead. 

  .. _method-editor_api-key_check_vb:

  \ **bool**\  *key_check_vb*\ (\ **int**\  player, \ **int**\  vb)

    Deprecated. Use :ref:`class input_api` instead. 

  .. _method-editor_api-key_check_pressed_vb:

  \ **bool**\  *key_check_pressed_vb*\ (\ **int**\  player, \ **int**\  vb)

    Deprecated. Use :ref:`class input_api` instead. 

  .. _method-editor_api-key_clear_vb:

  \ **void**\  *key_clear_vb*\ (\ **int**\  player, \ **int**\  vb)

    Deprecated. Use :ref:`class input_api` instead. 

  .. _method-editor_api-has_focus:

  \ **bool**\  *has_focus*\ ()

    Deprecated. Use :ref:`class input_api` instead. 

  .. _method-editor_api-is_polling_keyboard:

  \ **bool**\  *is_polling_keyboard*\ ()

    Deprecated. Use :ref:`class input_api` instead. 

  .. _method-editor_api-poll_keyboard:

  \ **bool**\  *poll_keyboard*\ ()

    Deprecated. Use :ref:`class input_api` instead. 

  .. _method-editor_api-editor_tab:

  \ **string**\  *editor_tab*\ ()

    Return the currently active editor tab. 

  .. _method-editor_api-editor_tab-2:

  \ **bool**\  *editor_tab*\ (\ **string**\  tab_name)

    Returns true if the change succeeded. 

  .. _method-editor_api-get_selected_layer:

  \ **int**\  *get_selected_layer*\ ()

    Returns the selected layer. 

  .. _method-editor_api-set_selected_layer:

  \ **void**\  *set_selected_layer*\ (\ **int**\  layer)

    Sets the selected layer. 

  .. _method-editor_api-get_layer_visible:

  \ **bool**\  *get_layer_visible*\ (\ **int**\  layer)

    Returns true if the given layer is visible. 

  .. _method-editor_api-set_layer_visible:

  \ **void**\  *set_layer_visible*\ (\ **int**\  layer, \ **bool**\  visible)

    Sets the visibility of the given layer. 

  .. _method-editor_api-get_layer_locked:

  \ **bool**\  *get_layer_locked*\ (\ **int**\  layer)

    Returns true if the given layer is locked. 

  .. _method-editor_api-set_layer_locked:

  \ **void**\  *set_layer_locked*\ (\ **int**\  layer, \ **bool**\  visible)

    Sets the locked state of the given layer. 

  .. _method-editor_api-check_layer_filter:

  \ **bool**\  *check_layer_filter*\ (\ **int**\  layer)

    Returns true if the given layer is visible and not locked. 

  .. _method-editor_api-get_selected_trigger:

  \ **entity**\ @ *get_selected_trigger*\ ()

    Returns the selected trigger. 

  .. _method-editor_api-get_selected_entity:

  \ **entity**\ @ *get_selected_entity*\ ()

    Returns the selected entity. 

  .. _method-editor_api-help_screen_vis:

  \ **bool**\  *help_screen_vis*\ ()

    Access whether the help menu is visible. 

  .. _method-editor_api-help_screen_vis-2:

  \ **void**\  *help_screen_vis*\ (\ **bool**\  vis)

  .. _method-editor_api-hide_gui:

  \ **bool**\  *hide_gui*\ ()

  .. _method-editor_api-hide_gui-2:

  \ **void**\  *hide_gui*\ (\ **bool**\  hide)

  .. _method-editor_api-hide_panels_gui:

  \ **bool**\  *hide_panels_gui*\ ()

  .. _method-editor_api-hide_panels_gui-2:

  \ **void**\  *hide_panels_gui*\ (\ **bool**\  hide)

  .. _method-editor_api-hide_toolbar_gui:

  \ **bool**\  *hide_toolbar_gui*\ ()

  .. _method-editor_api-hide_toolbar_gui-2:

  \ **void**\  *hide_toolbar_gui*\ (\ **bool**\  hide)

  .. _method-editor_api-hide_layers_gui:

  \ **bool**\  *hide_layers_gui*\ ()

  .. _method-editor_api-hide_layers_gui-2:

  \ **void**\  *hide_layers_gui*\ (\ **bool**\  hide)

  .. _method-editor_api-mouse_in_gui:

  \ **bool**\  *mouse_in_gui*\ ()

    Returns true if the mouse is within the editor GUI menus 

  .. _method-editor_api-force_mouse_in_gui:

  \ **void**\  *force_mouse_in_gui*\ ()

    Force the editor to act as if the mouse is inside of the GUI menu for the
    remainder of the frame 

  .. _method-editor_api-menu_left_panel_width:

  \ **int**\  *menu_left_panel_width*\ ()

    Returns the width of the left menu panel. 

  .. _method-editor_api-menu_right_panel_width:

  \ **int**\  *menu_right_panel_width*\ ()

    Returns the width of the right menu panel. 

  .. _method-editor_api-select_rectangle:

  \ **rectangle**\ @ *select_rectangle*\ ()

  .. _method-editor_api-selected_entity_count:

  \ **uint**\  *selected_entity_count*\ ()

    Return the number of selected entities. 

  .. _method-editor_api-selected_entity:

  \ **entity**\ @ *selected_entity*\ (\ **uint**\  index)

    Return the index-th selected entity or null if no entity exists at that index. 

  .. _method-editor_api-selected_prop_count:

  \ **uint**\  *selected_prop_count*\ ()

    Return the number of selected props. 

  .. _method-editor_api-selected_prop:

  \ **prop**\ @ *selected_prop*\ (\ **uint**\  index)

    Return the index-th selected prop or null if no prop exists at that index. 

class input_api
###############
  .. _method-input_api-get_text:

  \ **string**\  *get_text*\ ()

    Returns text input recorded over the last frame. 

  .. _method-input_api-set_text:

  \ **void**\  *set_text*\ (\ **string**\  text)

  .. _method-input_api-get_clipboard:

  \ **string**\  *get_clipboard*\ ()

    Returns the clipboard text. 

  .. _method-input_api-set_clipboard:

  \ **bool**\  *set_clipboard*\ (\ **string**\  text)

    Returns false on failure?? 

  .. _method-input_api-mouse_x_hud:

  \ **float**\  *mouse_x_hud*\ (\ **bool**\  scale)

    Returns the x coordinate of the mouse in the hud coordinate space. If scale
    is set to true will auto scale the coordinates to simulate a 1600-900
    screen size. Will range between -width/2 and width/2.
    

  .. _method-input_api-mouse_x_hud-2:

  \ **float**\  *mouse_x_hud*\ ()

    Equivalent to mouse_x_hud(false) 

  .. _method-input_api-mouse_y_hud:

  \ **float**\  *mouse_y_hud*\ (\ **bool**\  scale)

    Returns the y coordinate of the mouse in the hud coordinate space. If scale
    is set to true will auto scale the coordinates to simulate a 1600-900
    screen size. Will range between -height/2 and height/2.
    

  .. _method-input_api-mouse_y_hud-2:

  \ **float**\  *mouse_y_hud*\ ()

    Equivalent to mouse_y_hud(false) 

  .. _method-input_api-mouse_x_world:

  \ **float**\  *mouse_x_world*\ (\ **int**\  layer)

    Returns the x coordinate of the mouse for the given layer. 

  .. _method-input_api-mouse_y_world:

  \ **float**\  *mouse_y_world*\ (\ **int**\  layer)

    Returns the y coordinate of the mouse for the given layer. 

  .. _method-input_api-screen_width:

  \ **float**\  *screen_width*\ ()

    Return the current screen width in pixels. 

  .. _method-input_api-screen_height:

  \ **float**\  *screen_height*\ ()

    Return the current screen height in pixels. 

  .. _method-input_api-mouse_state:

  \ **int**\  *mouse_state*\ ()

    Returns the mouse state as a bitmask. The
    bits correspond to the following button states:
    
    Bitmask:
      :0x1: wheel up
      :0x2: wheel down
      :0x4: left down
      :0x8: right down
      :0x10: middle down
      :0x20: left pressed
      :0x40: right pressed
      :0x80: middle pressed
      :0x100: left release
      :0x200: right release
      :0x400: middle release
    

  .. _method-input_api-key_check_vk:

  \ **bool**\  *key_check_vk*\ (\ **int**\  vk)

    Returns true if the key is currently pressed. vk should be a
    virtual key keycode. See
    https://docs.microsoft.com/en-us/windows/win32/inputdev/virtual-key-codes.
    This is raw access to the underlying key state and will never work
    in net games. Button states should only be accessed in step() functions.
    

  .. _method-input_api-key_check_pressed_vk:

  \ **bool**\  *key_check_pressed_vk*\ (\ **int**\  vk)

    Returns true if the key was pressed this frame. 

  .. _method-input_api-key_check_released_vk:

  \ **bool**\  *key_check_released_vk*\ (\ **int**\  vk)

    Returns true if the key was released this frame. 

  .. _method-input_api-key_check_gvb:

  \ **bool**\  *key_check_gvb*\ (\ **int**\  gvb)

    Returns true if the "global virtual button" is currently pressed.
    Refer to the GLOBAL_VIRTUAL_BUTTON enum for options for this value.
    These button states are fully managed in net games.
    

  .. _method-input_api-key_check_pressed_gvb:

  \ **bool**\  *key_check_pressed_gvb*\ (\ **int**\  gvb)

    Returns true if the global virtual button is pressed this frame. 

  .. _method-input_api-key_check_released_gvb:

  \ **bool**\  *key_check_released_gvb*\ (\ **int**\  gvb)

    Returns true if the global virtual button is released this frame. 

  .. _method-input_api-key_clear_gvb:

  \ **void**\  *key_clear_gvb*\ (\ **int**\  gvb)

    Unset the global virtual button state. 

  .. _method-input_api-key_check_vb:

  \ **bool**\  *key_check_vb*\ (\ **int**\  player, \ **int**\  vb)

    Returns true if the "player virtual button" is currently pressed.
    Refer to the PLAYER_VIRTUAL_BUTTON enum for options for this value.
    These button states are fully managed in net games.
    

  .. _method-input_api-key_check_pressed_vb:

  \ **bool**\  *key_check_pressed_vb*\ (\ **int**\  player, \ **int**\  vb)

    Returns true if the global virtual button is pressed this frame. 

  .. _method-input_api-key_clear_vb:

  \ **void**\  *key_clear_vb*\ (\ **int**\  player, \ **int**\  vb)

    Unset the global virtual button state. 

  .. _method-input_api-has_focus:

  \ **bool**\  *has_focus*\ ()

    Returns true if a UI control has focus 

  .. _method-input_api-is_polling_keyboard:

  \ **bool**\  *is_polling_keyboard*\ ()

    Returns true if a UI control,
    e.g. a text box, is taking keyboard input
    

  .. _method-input_api-poll_keyboard:

  \ **bool**\  *poll_keyboard*\ ()

    Polls the keyboard for one frame, blocking shortcuts such as
    frame advance
    

class nexus_api
###############
  .. _method-nexus_api-get_keys_used:

  \ **void**\  *get_keys_used*\ (\ **int**\  &out wood, \ **int**\  &out silver, \ **int**\  &out gold, \ **int**\  &out red, \ **bool**\  &out ngplus)

    Get the number of keys that have been used of each time. This reflects
    directly what is persisted to disk. ngplus controls whether all doors
    are automatically in an open state.
    

  .. _method-nexus_api-set_keys_used:

  \ **void**\  *set_keys_used*\ (\ **int**\  wood, \ **int**\  silver, \ **int**\  gold, \ **int**\  red, \ **bool**\  ngplus)

    Update key usage and save to disk. 

  .. _method-nexus_api-get_keys_earned:

  \ **void**\  *get_keys_earned*\ (\ **int**\  &out wood, \ **int**\  &out silver, \ **int**\  &out gold, \ **int**\  &out red)

    Convenience function to calculate number of keys that have been earned
    of each type. Subtract out the used key counts to get the number of
    available keys. 

  .. _method-nexus_api-score_count:

  \ **uint**\  *score_count*\ ()

    Get count of levels that have score data in this nexus root 

  .. _method-nexus_api-score_level:

  \ **string**\  *score_level*\ (\ **uint**\  index)

    Get the name of the i-th level in this nexus root 

  .. _method-nexus_api-score_lookup:

  \ **bool**\  *score_lookup*\ (\ **string**\  level, \ **int**\  &out thorough, \ **int**\  &out finesse, \ **float**\  &out time, \ **int**\  &out key_type)

    Lookup the score data for a given level 

  .. _method-nexus_api-score_set:

  \ **void**\  *score_set*\ (\ **string**\  level, \ **int**\  thorough, \ **int**\  finesse, \ **float**\  time, \ **int**\  key_type)

    Set the score data for a given level 

