23.1.1
======

General
-------

  - Fix possible lag when a single plugin is enabled.
  - Fix out of bounds exception for invalid tile set/index (Allows permanent
    invisible tiles by setting the tile set to 0 and tile index to a non-zero
    value).
  - Fix possible crash and invisible sweep sprite when changing character mid-level.


Tools
-----
  - Use Alt+F1 to switch to plugin dev mode. In this mode `F1` will instead
    compile the previously compiled plugin.
  - Console can be scrolled.
    - PageUp/Down and Shift+Home/End also supported.
    - Zoom is now Ctrl+Scroll.
  - Add console `watch` command - like inspect but displays the results live in the hud.
  - Fix crash when copying with nothing selected in the console.

Editor
------
  - Ctrl/Alt click to copy/paste particle settings - emitter names, individual
    emitters, and particle types can all be copied and pasted.
  - Ctrl+Drag certain particle editor sliders to adjust the min/max range.
    - Ctrl+Right click to reset the range.
  - Allow non-45 degree particle gravity.
  - Wrap drop down lists that don't fit on screen.
  - Select Tool - Right click to single select type.
  - Add editor trigger and camera visibility options
  - Script type lists are now in alphabetical order.
  - Output alpha value in colour picker hex input.
  - Add auto launch console option.
  - Alt+Right click a script name to move it to the top.
  - Fix text prop handle active colour.
  - Fix scriptenemy menus not scrollable.

Dustscript API
--------------
  - Improve play/edit/restart times by only rebuilding embeds on level load.
  - Add multiplayer :ref:`checkpoint_save <method-script-checkpoint_save-2>` and
    :ref:`checkpoint_load <method-script-checkpoint_load-2>` callbacks.
  - Add :ref:`prop.sub_layer <method-prop-sub_layer>` get/set methods.
  - Add :ref:`editor_api.get_selected_sub_layer <method-editor_api-get_selected_sub_layer>`
    and :ref:`editor_api.set_selected_sub_layer <method-editor_api-set_selected_sub_layer>`.
  - Add :ref:`trigger_base.editor_init <method-trigger_base-editor_init>` and
    :ref:`enemy_base.editor_init <method-enemy_base-editor_init>` methods.
  - Add :ref:`entity.centre <method-entity-centre>` get/set methods
  - Add :ref:`controllable.fric <method-controllable-fric>` - Used by some
    enemies to control air, turn, or attack friction.
  - Move physics values :ref:`run_max <method-controllable-run_max>`,
    :ref:`run_start <method-controllable-run_start>`, :ref:`run_accel
    <method-controllable-run_accel>`, :ref:`idle_fric
    <method-controllable-idle_fric>`, and :ref:`skid_fric
    <method-controllable-skid_fric>` from :ref:`dustman <class-dustman>` to
    :ref:`controllable <class-controllable>`
  - Slight performance improvement to `scene::draw_xx_world` methods (replaced
    wrapper methods with direct calls)

Engine
------
  - Windows builds will automatically attach to parent console when run from the console
