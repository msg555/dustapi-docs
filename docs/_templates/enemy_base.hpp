/* STARTAPI */
/* Extend this class to create a new type of script-backed enemy.
 * 
 * See :ref:`trigger_base<class trigger_base>` documentation for discussion on
 * member variables. */
class enemy_base {
  /* Setup initial variables. An empty constructor must be present (unless
   * there are no constructors at all in which a default one is implied) for
   * enemies to be usable. */
  enemy_base();

  /* Called after the enemy is constructed, passing the corresponding game
   * :ref:`scriptenemy<class scriptenemy>` handle. */
  void init(script@ s, scriptenemy@ self);

  /* Called after the entity has been added to the scene. */
  void on_add();

  /* Called after the entity has been removed from the scene. */
  void on_remove();

  /* Called when the scale of the object has changed and collisions should be
   * updated. */
  void on_change_scale(float new_scale);

  /* Called when the enemy is stepped. */
  void step();

  /* Called when the enemy is stepped while in editor mode. */
  void editor_step();

  /* Do drawing related to the enemy. */
  void draw(float sub_frame);

  /* Do drawing in the editor related to the enemy trigger. */
  void editor_draw(float sub_frame);

  /* Called when one of this enemy's variables is modified in the editor */
  void editor_var_changed(var_info@ info);

  /* Called when a message has been sent to the entity with
   * ``entity.send_message(id, @msg)``. */
  void on_message(string id, message@ msg);

}
/* STOPAPI */
