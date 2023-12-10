23.10.1
======

General
-------

	- Add a new `Script Fx Level` setting to video options which can be used by scripts to disable performance intensive visuals.
	- Spikes and dust are rendered on invisible tiles.
	- Escape from the login menu will login as guest.
	- Fix tire hitboxes persisting after death.
	- Fix double splits in multiplayer.
	- Improve checkpoint performance on maps with large embeds.


Editor
------

	- Invisible tiles are visible in the editor.
	- Invisible tiles can be placed with the tile tool.
	- Add map option to persist particle settings with levels/checkpoints.
	- Rectangular Dustmod triggers.
		- Use the Aux key to toggle.
		- Alt to scale from centre.
	- Resizing and changing trigger shapes can now be undone.
	- Ctrl+Shift+Z can now also be used for redo.
	- Fit music trigger list size to screen.
	- Directly copy and paste fog colours by right clicking and alt+right clicking on layer swatches.
	- Remember script editor scroll position and array indices across compiles.
	- Draw tile tool marker while holding Alt.
	- Disable saving in play mode.
	- Remove reset all props scale shortcut key.
	- Allow prop etc. tools to function when GUI panels are hidden.
	- Fix tile tool cancelled when released over GUI.
	- Fix angle snapping for ranged circle controls.

Dustscript API
--------------

	- Layer annotation improvements:
		- `Shift`, `Control`, and `Alt` can now be used to snap coordinates to increments 48, 24, and 12 respectively.
		- A sublayer can optionally be specified with the format `LAYER.SUBLAYER`
		- **LAYER** or **SUBLAYER** can point to a variable by prefixing with an equal sign, e.g. `=layer_var_name.10` will read the layer value from a variable called `layer_var`, and use a value of 10 for the sublayer.
		- If **LAYER** is set to `selected`, the currently selected layer in the editor will be used.
		- **snap** If set forces a specific increment to snap the coordinates to.
		- **round** Can be `down`/`-1` or `up`/`1` to round down or up when snapping.
		- **tiles** If present will return the tile index under the mouse.
		- **relative** If present coordinates will be relative to the trigger/entity this property belongs to.
	- Add API to change sub layer :ref:`scale <method-scene-sub_layer_scale>` and
	  :ref:`visibility <method-scene-sub_layer_visible>`.
	- Add :ref:`key_check_double <method-input_api-key_check_double>`.
	- Add direct player input access through :ref:`camera::input_* <method-camera-input_x>` methods.
	- Add access to the particle system settings.
		- `Example usage <https://gist.github.com/cmann1/76ff4fc47262935246f294c218564dd3>`_
	- Add :ref:`on_video_settings_change <method-script-on_video_settings_change>` callback.
	- Add :ref:`get_script_fx_level <method-scene-get_script_fx_level>` and :ref:`get_video_settings <method-scene-get_video_settings>` methods to read user video settings.
	- Add various :ref:`fog_setting <class-fog_setting>` improvements.
		- :ref:`create_fog_setting() <func-create_fog_setting>` functions
		- Added :ref:`has_sub_layers <method-fog_setting-has_sub_layers>`
		- Added :ref:`layer_colour <method-fog_setting-layer_colour>` and :ref:`default_colour <method-fog_setting-default_colour>` for getting and setting the default sublayer colour.
		- Added :ref:`layer_percent <method-fog_setting-layer_percent>` and :ref:`default_percent <method-fog_setting-default_percent>` for getting and setting the default sublayer percent.
		- Added :ref:`copy_to <method-fog_setting-copy_to>` and :ref:`copy_from <method-fog_setting-copy_from>` for copying to and from cameras, fog triggers, and other `fog_settings`.
	- Add new methods for changing fog, music, and ambience.
		- :ref:`camera.change_fog <method-camera-change_fog>`
		- :ref:`camera.change_music <method-camera-change_music>`
		- :ref:`camera.change_ambience <method-camera-change_ambience>`
	- Add new :ref:`ai_controller <class-ai_controller>` class.
		- :ref:`controllable.ai_controller() <method-controllable-ai_controller>` returns the controllable's current controller.
	- Add :ref:`get_emitter_type_id <method-scene-get_emitter_type_id>` and :ref:`add_particle_burst <method-scene-add_particle_burst>` methods.
	- Fix :ref:`draw_line_world <method-scene-draw_line_world>` and :ref:`draw_line_hud <method-scene-draw_line_hud>` rounding down the line width, now allowing allowing non-integer thickness.
	- Fix non-allocating version of :ref:`ray_cast_tiles <method-scene-ray_cast_tiles-2>` incorrectly allocating new `tileinfo` objects.

Editor API
----------

	- Add :ref:`on_editor_start <method-script-on_editor_start>` which gets called after persisted variables have been loaded in the editor.
	- Add setters for the selected :ref:`entity <method-editor_api-set_selected_entity>` and :ref:`trigger <method-editor_api-set_selected_trigger>` in the editor.
	- Add access to selected editor tile and prop set.
		- :ref:`get_tile_sprite <method-editor_api-get_tile_sprite>` and :ref:`set_tile_sprite <method-editor_api-set_tile_sprite>`
		- :ref:`get_prop <method-editor_api-get_prop>` and :ref:`set_prop <method-editor_api-set_prop>`
	- Add :ref:`triggers_visible <method-editor_api-triggers_visible>` and :ref:`cameras_visible <method-editor_api-cameras_visible>` methods to check the visibility of the trigger and camera layers in the editor.
		- Convenience methods :ref:`editor_triggers_visible <method-scripttrigger-editor_triggers_visible>` and :ref:`editor_cameras_visible <method-scripttrigger-editor_cameras_visible>` to :ref:`scripttrigger <class-scripttrigger>` and :ref:`scriptenemy <class-scriptenemy>`
	- Add :ref:`gvb_to_vk <method-input_api-gvb_to_vk>` and :ref:`vk_to_gvb <method-input_api-vk_to_gvb>` methods to convert between global virtual buttons and key codes.
	- Add entity editor callbacks
		- :ref:`editor_entity_on_create <method-script-editor_entity_on_create>`
		- :ref:`editor_entity_on_add <method-script-editor_entity_on_add>`
		- :ref:`editor_entity_on_remove <method-script-editor_entity_on_remove>`
	- All whitespace inside annotations is now ignored, so it's now possible to split longer annotations across lines.
	- Allow unescaped alternate quotes inside attributes. (e.g. in `["can't"]` the single quote now doesn't need to be escaped.)
	- Correctly support `[option]` ids that are non-sequential or non-zero based.
	- Integer `[option]` s without values will now auto increment starting at zero, or from the last defined value.
	- Reduce default tooltip scale, and add tooltip attribute `scale` option.
