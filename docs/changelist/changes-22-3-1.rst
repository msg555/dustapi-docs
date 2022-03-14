22.3.1
======

General
-------

  - Fix missing editor anywhere keybind option
  - Block ctrl/shift/alt from being used as modifier if bound to base controls
  - Avoid showing combo bar in nexus levels in some circumstances

Editor
------
  - Fix alpha handling in colour picker

Dustscript API
--------------
  - Fix input api scroll to not miss scrolling
  - Fix camera not resizing when script camera is enabled
  - Fix crash in hit callback on quills
  - Add :ref:`hittable <class-hittable>` to the entity hierarchy as the parent of :class:`controllable`
  - Add :ref:`hitbox.on_hit_filter_callback <method-hitbox-on_hit_filter_callback>` to allow fine grain control over hitbox outcomes
  - Fix canvas::rotate methods not rotating correctly around the passed center
  - Add :ref:`scene.time_in_level <method-scene-time_in_level>`
  - Add :ref:`script.step_fixed <method-script-step_fixed>` to allow scripts to run while game is paused
  - Added :ref:`effect <class-effect>` class.
