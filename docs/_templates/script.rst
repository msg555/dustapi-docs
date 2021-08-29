Script Definition
#################

::

  /* Empty script with all callbacks. */

  class script {
    script() {
      /* Initialize any state variables here. */
    }

    void checkpoint_save() {
      /* Called just prior to a checkpoint being saved. */
    }

    void checkpoint_load() {
      /* Called after a checkpoint has been loaded. All entities and prop objects
       * will have been recreated and therefore existing handles will no longer
       * refer to objects in the scene and should be requeried. */
    }

    void entity_on_add(entity@ e) {
      /* Called when an entity is added to the scene. */
    }

    void entity_on_remove(entity@ e) {
      /* Called when an entity is removed from the scene. */
    }

    void move_cameras() {
      /* Called before the entity list to process has been constructed as an
       * opportunity to move the camera. Moving the camera in step() will
       * be too late to affect what segments and entities are loaded and stepped.
       */
    }

    void step(int entities) {
      /* Called every frame (60fps) prior to all entities having their step
       * function called. The list of entities going to be stepped can be accessed
       * with entity_by_index(i) for 0 <= i < entities.
       */
    }

    void step_post(int entities) {
      /* Like step except called after all entities have had their step functions
       * called. */
    }

    void pre_draw(float sub_frame) {
      /* Setup the camera/transform prior to anything being drawn. Do not actually
       * draw anything here. */
    }

    void draw(float sub_frame) {
      /* Do any drawing required by your script. This function should have no side
       * effects outside of the draw calls it makes. */
    }

    void editor_step() {
      /* Called each frame while in the editor instead of step/step_post. */
    }

    void editor_pre_draw(float sub_frame) {
      /* Called each pre draw frame while in the editor instead of pre_draw. */
    }

    void editor_draw(float sub_frame) {
      /* Called each draw frame while in the editor instead of draw. */
    }

    void editor_var_changed(var_info@) {
      /* Called when one of this script's variables is modified in the editor */
    }

    void spawn_player(message@ msg) {
      /* Spawn a player controllable. The following parameters will be set
       * in the passed message:
       *   msg.get_float("x"): The x coordinate to spawn the player.
       *   msg.get_float("y"): The y coordinate to spawn the player.
       *   msg.get_int("player"): The player index of the player.
       *   msg.get_float("character"): The character id of the selected player
       *                               (e.g. "dustgirl")
       * The following fields can be set to create your player object:
       *   msg.set_entity(@pl): Set the spawned player controllable.
       */
    }

    void build_sprites(message@ msg) {
      /* Used to set custom sprite data from embedded values. See
       * has_embed_value() for more details on how to embed a value. Sprites
       * should be in PNG format.
       *
       * For each sprite you wish to create add a string to the message with the
       * desired sprite name as the key and the embed key as the value.
       * Additionally you can specify custom 'offset' coordinates into the sprite
       * to define where the center of the sprite is (defaults to (0, 0)) by
       * setting an int key of the form "sprite_name|offsetx" and
       * "sprite_name|offsety".
       *
       * See https://gist.github.com/msg555/3aaa96428d964c1612b540c208c3ad1e for
       * a complete example on how to embed, build, and use custom sprites.
       */
    }

    void build_sounds(message@ msg) {
      /* Userd to set custom sound data from embedded values similar to
       * build_sprites.
       *
       * For each sound you wish to create add a string to the message with the
       * desired sound name as the key and the embed key as the value.
       * Additionally you can specify a custom loop point (measured in samples at
       * 44.1 kHz) by setting an int key of the form "sound_name|loop".
       *
       * See https://gist.github.com/msg555/821c3aec14852e67fd15c7ec96a851f2 for
       * a complete example of how to embed, build, and use custom sounds.
       */
    }

    void on_level_start() {
      /* Called when the level begins play either by loading the level normally or
       * by tabbing in from the editor. */
    }

    void on_level_end() {
      /* Called when an end condition for the level has been triggered and the
       * replay is about to be uploaded. You may still modify plugin_score at
       * this point. */
    }

    void editor_loaded() {
      /* Called when entering editor mode. Only applicable to editor plugins */
    }

    void editor_unloaded() {
      /* Called before entering play mode. Only applicable to editor plugins */
    }

  }

Trigger Definition
##################

::

  /* A script-backed trigger. */
  class mytrigger : trigger_base {
    scripttrigger@ self;

    /* Non handle variables can be persisted and made editable in the editor
     * using annotations. These annotated values will be modifiable in the editor
     * and persisted across checkpoints. These values will be set by the time
     * init() is called. You should still set sensible defaults in the object's
     * constructor.
     *
     * You can control how a variable is modified in the editor using annotations.
     * Annotations appear before the variable declaration and can take additional
     * parameters afterwards.
     * Variable name labels will be CamelCased and underscores removed by default.
     * Keys or values that have spaces in them must be wrapped in single or double
     * quotes.
     *
     * Multiple annotations can be added to a single variable by separating
     * them with '|':
     *   [attribute1|attribute2|...]
     * Useful for example when adding a tooltip to a variable that already has
     * other annotations:
     *   [color,alpha|tooltip:'Select a colour']
     *
     * Certain attributes take a colour value in the form of a hex value,
     * AARRGGBB or ARGB.
     * Alpha values are optional and will default to 0xFF. The optional prefixes
     * '#' and '0x' are also allowed.
     *
     * Here is the full list of supported annotations
     * (fields in all caps are meant to be customized).
     *
     *
     * [hidden]
     *   Persist the variable but don't show it in the editor.
     *   Can also be added to classes to hide it in the editor's
     *   type select menu.
     * [label:TEXT]
     *   Use TEXT for the variables label instead of the variable's name.
     * [tooltip:TEXT,delay:DELAY,font:STRING,size:INT,colour/color:COLOUR]
     *   Will display the tooltip TEXT after DELAY frames (default 20).
     *   Fields with a tooltip will be highlighted in blue.
     *   Optionaly the font, size, and colour can be set. For a list of
     *   valid font/size pairs, see https://pastebin.com/YcNKSXd9
     * [text]
     *   Use a simple text field to modify the variable. This is the default
     *   annotation
     * [option,VALUE1:OPTION1,VALUE2:OPTION2,...]
     *   Use a dropdown option menu. If the user selects OPTIONk the variable's
     *   value will be set to VALUEk.
     * [angle,MODE]
     *   Use to set an angle. MODE can be set to 'rad' or 'radian' to use radians
     *   otherwise it defaults to degrees.
     * [color,alpha] or [colour,alpha]
     *   Use to specify a colour parameter. The optional 'alpha' parameter will
     *   display a slider allowing the colour's alpha channel to be changed,
     *   otherwise it will always set to 0xFF.
     * [slider,min:MINVAL,max:MAXVAL]
     *   Use a slider element to set a value between MINVAL and MAXVAL uniformly
     *   distributed.
     * [position,mode:MODE,layer:LAYER,y:YPARAM]
     *   Use this annotation on an x-variable, naming the corresponding y variable
     *   as YPARAM. MODE can be 'world' or 'hud', defaulting to 'world'. LAYER is
     *   the layer to calculate the coordinates of from the user's mouse.
     * [fixed:MODE]
     *   If present it will not be possible to add or remove items from arrays.
     *   MODE can be 'all' (default), or 'top'.
     *   If MODE is 'top', only the top level of a multidimensional array will be
     *   fixed and subsequent levels will be modifiable.
     *
     * Additionally, bools, arrays, and non-handle classes have the following
     * semantics.
     *
     * bools
     *   Always use a checkbox UI if a non-hidden annotation is supplied.
     *
     * arrays
     *   The annotation applied to the array is instead applied to the value
     *   within the array and an array wrapper UI is used.
     *
     * classes
     *   Always use a class UI if a non-hidden annotation is supplied.
     *
     * Variables will appear in the editor in declaration order. You can
     * override this behavior using the order using an annotation before
     * the start of the class definition that looks like:
     * [order:[pizza,colour,other_entity_id]]
     * Any missing parameters will be added afterwards in alphabetical order.
     */
    [entity] int other_entity_id;
    [hidden] string my_hidden_string;
    [option,0:Cheese,1:Pepperoni,2:Mushroom] int pizza;
    [angle] float direction_in_degrees;
    [angle,radian] float direction_in_radians;
    [colour] int colour;
    [slider,min:0,max:55.5] float slider_val;

    [position,mode:world,layer:19,y:pos_y] float pos_x;
    [hidden] float pos_y; // Declare the var hidden so it is persisted.

    mytrigger() {
      /* Setup initial variables. An empty constructor must be present (unless
       * there are no constructors at all in which a default one is implied) for
       * triggers to be usable. */
    }

    void init(script@ s, scripttrigger@ self) {
      /* Called after the trigger is constructed, passing the corresponding game
       * scripttrigger handle. */
      @this.self = @self;
    }

    void on_add() {
      /* Called after the entity has been added to the scene. */
    }

    void on_remove() {
      /* Called after the entity has been removed from the scene. */
    }

    void step() {
      /* Called when the trigger is stepped. */
    }

    void editor_step() {
      /* Called when the trigger is stepped while in editor mode. */
    }

    void editor_var_changed(var_info@) {
      /* Called when one of this trigger's variables is modified in the editor */
    }

    void draw(float sub_frame) {
      /* Do drawing related to the script trigger. */
    }

    void editor_draw(float sub_frame) {
      /* Do drawing in the editor related to the script trigger. The base
       * implementation will draw a square for the trigger and, if the activate()
       * function is present, the trigger radius. */
    }

    void editor_var_changed(var_info@) {
      /* Called when a variable is edited in the editor */
    }

    void activate(controllable@ e) {
      /* Called when any controllable object within the region associated with
       * the trigger. activate() is called for each object each frame it is within
       * the trigger. */
    }

    void on_message(string id, message@ msg) {
      /* Called when a message has been sent to the entity with
       * entity.send_message(id, @msg). */
    }
  }


Enemy Definition
################

::

  class myenemy : enemy_base {
    /* See triger_base documentation for discussion on member variables. */

    myenemy() {
      /* Setup initial variables. An empty constructor must be present (unless
       * there are no constructors at all in which a default one is implied) for
       * enemies to be usable. */
    }

    void init(script@ s, scriptenemy@ self) {
      /* Called after the enemy is constructed, passing the corresponding game
       * controllable handle. */
    }

    void on_add() {
      /* Called after the entity has been added to the scene. */
    }

    void on_remove() {
      /* Called after the entity has been removed from the scene. */
    }

    void on_change_scale(float new_scale) {
      /* Called when the scale of the object has changed and collisions should be
       * updated. */
    }

    void step() {
      /* Called when the enemy is stepped. */
    }

    void editor_step() {
      /* Called when the enemy is stepped while in editor mode. */
    }

    void draw(float sub_frame) {
      /* Do drawing related to the enemy. */
    }

    void editor_draw(float sub_frame) {
      /* Do drawing in the editor related to the enemy trigger. */
    }

    void editor_var_changed(var_info@) {
      /* Called when one of this enemy's variables is modified in the editor */
    }

    void on_message(string id, message@ msg) {
      /* Called when a message has been sent to the entity with
       * entity.send_message(id, @msg). */
    }
  }
