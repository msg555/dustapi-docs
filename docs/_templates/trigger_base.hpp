/* STARTAPI */
/* Extend this class to create a new type of script-backed trigger.
 * 
 * Non handle variables can be persisted and made editable in the editor
 * using annotations. These annotated values will be modifiable in the editor
 * and persisted across checkpoints. These values will be set by the time
 * :ref:`init()<method-trigger_base-init>` is called.
 * You should still set sensible defaults in the object's constructor.
 *
 * You can control how a variable is modified in the editor using annotations.
 * Annotations appear before the variable declaration and can take additional
 * parameters afterwards.
 * Variable name labels will be CamelCased and underscores removed by default.
 * Keys or values that have spaces in them must be wrapped in single or double
 * quotes.
 *
 * Multiple annotations can be added to a single variable by separating
 * them with "|": ``[attribute1|attribute2|...]``

 * Useful for example when adding a tooltip to a variable that already has
 * other annotations: ``[color,alpha|tooltip:'Select a colour']``

 * Certain attributes take a colour value in the form of a hex value,
 * ``AARRGGBB`` or ``ARGB``.
 * Alpha values are optional and will default to 0xFF. The optional prefixes
 * "#"" and "0x" are also allowed.
 *
 * Here is the full list of supported annotations
 * (fields in all caps are meant to be customized).
 *
 * [hidden]
 *   Persist the variable but don't show it in the editor.
 *   Can also be added to classes to hide it in the editor's
 *   type select menu.
 * [label:**TEXT**]
 *   Use **TEXT** for the variables label instead of the variable's name.
 * [tooltip:**TEXT**,delay:DELAY,font:STRING,size:INT,colour/color:COLOUR]
 *   Will display the tooltip **TEXT** after **DELAY** frames (default 20).
 *   Fields with a tooltip will be highlighted in blue.
 *   Optionaly the font, size, and colour can be set. For a list of
 *   valid font/size pairs, see https://pastebin.com/YcNKSXd9
 * [text]
 *   Use a simple text field to modify the variable. This is the default
 *   annotation
 * [option,VALUE1:OPTION1,VALUE2:OPTION2,...]
 *   Use a dropdown option menu. If the user selects **OPTIONk** the
 *   variable's value will be set to **VALUEk**.
 * [angle,MODE]
 *   Use to set an angle. **MODE** can be set to 'rad' or 'radian' to use
 *   radians otherwise it defaults to degrees.
 * [color,alpha] or [colour,alpha]
 *   Use to specify a colour parameter. The optional **alpha** parameter will
 *   display a slider allowing the colour's alpha channel to be changed,
 *   otherwise it will always set to 0xFF.
 * [slider,min:MINVAL,max:MAXVAL,step:STEP]
 *   Use a slider element to set a value between **MINVAL** and **MAXVAL**
 *   uniformly distributed, or with a custom interval using **STEP**.
 * [position,mode:MODE,layer:LAYER,y:YPARAM]
 *   Use this annotation on an x-variable, naming the corresponding y
 *   **variable** as **YPARAM**. **MODE** can be "world" or "hud", defaulting
 *   to "world". **LAYER** is the layer to calculate the coordinates of from
 *   the user's mouse.
 * [entity,TYPE,TYPE,...]
 *   | Use to select an entity id with the mouse.
 *   | An optional list of allowed types can be given. If no **TYPE** type is
 *     specified the defaults are hittable entities and triggers.
 *   | The following values are supported:
 *   |   ``default``, ``player``, ``enemy``, ``trigger``, ``camera``,
 *       ``emitter``, ``flags``, ``kill_zone``
 * [fixed:MODE]
 *   If present it will not be possible to add or remove items from arrays.
 *   **MODE** can be "all" (default), or "top".
 *   If **MODE** is "top", only the top level of a multidimensional array will
 *   be fixed and subsequent levels will be modifiable.
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
 * ``[order:[pizza,colour,other_entity_id]]``
 * Any missing parameters will be added afterwards in alphabetical order.
 * 
 * Examples:
 * 
 * .. code-block:: c++
 * 
 *   [entity] int other_entity_id;
 *   [hidden] string my_hidden_string;
 *   [option,0:Cheese,1:Pepperoni,2:Mushroom] int pizza;
 *   [angle] float direction_in_degrees;
 *   [angle,radian] float direction_in_radians;
 *   [colour] int colour;
 *   [slider,min:0,max:55.5] float slider_val;
 *   
 *   [position,mode:world,layer:19,y:pos_y] float pos_x;
 *   [hidden] float pos_y; // Declare the var hidden so it is persisted.
 *
 * Your trigger must have an empty constructor. (unless
 * there are no constructors at all in which a default one is implied) for
 * the trigger to be usable.
 */
class trigger_base {
  /* Called only in the editor when a type is selected, before before init.
   * Can be used to initialise persistent variables which require access to the
   * script or script trigger instance. */
  void editor_init(script@ s, scripttrigger@ self);
  
  /* Called after the trigger is constructed, passing the corresponding game
   * :ref:`scripttrigger<class scripttrigger>` handle. */
  void init(script@ s, scripttrigger@ self);
  
  /* Called after the entity has been added to the scene. */
  void on_add();
  
  /* Called after the entity has been removed from the scene. */
  void on_remove();
  
  /* Called when the trigger is stepped. */
  void step();
  
  /* Called when the trigger is stepped while in editor mode. */
  void editor_step();
  
  /* Called when one of this trigger's variables is modified in the editor */
  void editor_var_changed(var_info@ info);
  
  /* Do drawing related to the script trigger. */
  void draw(float sub_frame);
  
  /* Do drawing in the editor related to the script trigger. The base
   * implementation will draw a square for the trigger and, if the activate()
   * function is present, the trigger radius. */
  void editor_draw(float sub_frame);
  
  /* Called when one of this trigger's variables is modified in the editor */
  void editor_var_changed(var_info@ info);
  
  /* Called when any controllable object within the region associated with
   * the trigger. :ref:`activate()<method-trigger_base-activate>` is called
   * for each object each frame it is within the trigger. */
  void activate(controllable@ e);
  
  /* Called when a message has been sent to the entity with
   * ``entity.send_message(id, @msg)``. */
  void on_message(string id, message@ msg);
}
/* STOPAPI */
