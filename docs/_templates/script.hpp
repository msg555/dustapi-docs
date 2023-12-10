/* STARTAPI */
/* The entry point - each script must have a single class named *script*. */
class script {
  /* Initialize any state variables here. */
  script();

  /* Called just prior to a checkpoint being saved. */
  void checkpoint_save();

  /* Called after a checkpoint has been loaded. All entities and prop objects
   * will have been recreated and therefore existing handles will no longer
   * refer to objects in the scene and should be requeried. */
  void checkpoint_load();

  /* Called when a player hits a checkpoint during multiplayer. */
  void checkpoint_save(int player_index);

  /* Called when a player is respawned during multiplayer. */
  void checkpoint_load(int player_index);

  /* Called when an entity is added to the scene. */
  void entity_on_add(entity@ e);

  /* Called when an entity is removed from the scene. */
  void entity_on_remove(entity@ e);

  /* Called before the entity list to process has been constructed as an
   * opportunity to move the camera. Moving the camera in
   * :method:`script.step` will be too late to affect what segments
   * and entities are loaded and stepped.
   */
  void move_cameras();

  /* Called every game frame (usually 60fps) prior to all entities having their step
   * function called. The list of entities going to be stepped can be accessed
   * with :func:`entity_by_index`(i) for ``0 <= i < entities``.
   */
  void step(int entities);

  /* Like step except called after all entities have had their step functions
   * called. */
  void step_post(int entities);

  /* This function is called at 60fps even when the game menu is opened,
   * slowed during fade out, loading checkpoints, etc. This is still
   * subject to manipulation from pausing/changing game speed with frame
   * advance, however. This mirrors the behavior of the menu subsystem.
   */
  void step_fixed();

  /* Setup the camera/transform prior to anything being drawn. Do not actually
   * draw anything here. */
  void pre_draw(float sub_frame);

  /* Do any drawing required by your script. This function should have no side
   * effects outside of the draw calls it makes. */
  void draw(float sub_frame);

  /* Called each frame while in the editor instead of step/step_post. */
  void editor_step();

  /* Called each pre draw frame while in the editor instead of pre_draw. */
  void editor_pre_draw(float sub_frame);

  /* Called each draw frame while in the editor instead of draw. */
  void editor_draw(float sub_frame);

  /* Called when one of this script's variables is modified in the editor */
  void editor_var_changed(var_info@ info);

  /* Called when an entity is added to the scene in the editor. */
  void editor_entity_added(entity@ e);

  /* Called when an entity is removed from the scene in the editor. */
  void editor_entity_remove(entity@ e);

  /* Spawn a player controllable. The following parameters will be set
   * in the passed message:
   * 
   * :float x: The x coordinate to spawn the player
   * :float y: The y coordinate to spawn the player
   * :int player: The player index of the player
   * :string character: The character id of the selected player
   *   (e.g. "dustgirl")
   * 
   * The following fields can be set to create your player object:
   * 
   * :entity@ player: Set the spawned player controllable.
   * 
   */
  void spawn_player(message@ msg);

  /* Used to set custom sprite data from embedded values. See
   * :func:`has_embed_value`() for more details on how
   * to embed a value. Sprites should be in PNG format.
   *
   * For each sprite you wish to create add a string to the message with the
   * desired sprite name as the key and the embed key as the value.
   * Additionally you can specify custom "offset" coordinates into the sprite
   * to define where the center of the sprite is (defaults to (0, 0)) by
   * setting an int key of the form "sprite_name|offsetx" and
   * "sprite_name|offsety".
   *
   * See https://gist.github.com/msg555/3aaa96428d964c1612b540c208c3ad1e for
   * a complete example on how to embed, build, and use custom sprites.
   */
  void build_sprites(message@ msg);

  /* Userd to set custom sound data from embedded values similar to
   * :ref:`build_sprites()<method-script-build_sprites>`.
   *
   * For each sound you wish to create add a string to the message with the
   * desired sound name as the key and the embed key as the value.
   * Additionally you can specify a custom loop point (measured in samples at
   * 44.1 kHz) by setting an int key of the form "sound_name|loop".
   *
   * See https://gist.github.com/msg555/821c3aec14852e67fd15c7ec96a851f2 for
   * a complete example of how to embed, build, and use custom sounds.
   */
  void build_sounds(message@ msg);

  /* Called when the level begins play either by loading the level normally or
   * by tabbing in from the editor. */
  void on_level_start();

  /* Called when an end condition for the level has been triggered and the
   * replay is about to be uploaded. You may still modify plugin_score at
   * this point. */
  void on_level_end();

  /* Called when entering editor mode. Only applicable to editor plugins */
  void editor_loaded();

  /* Called before entering play mode. Only applicable to editor plugins */
  void editor_unloaded();

}
/* STOPAPI */
