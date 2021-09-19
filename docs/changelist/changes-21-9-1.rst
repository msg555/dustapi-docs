21.9.1
======

General
-------

	- Fix save/load state crash when using script has a `timedate@` field
	- Fix unloaded entities still being detected by end flags in Dustmod
	- Fix DX12 device error
	- Fix segments overwriting checkpoint when unloading
	- Fix player movement FX positions when player is scaled
	- Fix weird tome scroll behaviour when using arrow keys after searching
	- Fix score screen not shown for OOB/unload
	- Fix crashes related to embeds
	- Fix escape respawning player 1 in multiplayer
	- Improve/Fix blurry text compared to vanilla
	- OOB/Unload now works on dustmod maps
	- Door/tome titles will no longer overlap in multiplayer - only the title for the active camera is drawn
	- PIP rendered using the PIP camera fog, instead of the main camera fog
	- Clipboard support - text can now be copied and pasted into text boxes and triggers
	- In game console (F12)
		- Type "help" for a list of commands
		- Ctrl + F12 to open normal console
	- Support for modifiers in Dustmod key bindings (double tapping a modifier can be used to bind the modifier key itself)

Tools
-----
	- Fix text trigger text not drawn when **Show Triggers** is on
	- Fix dragging debug camera lag when game speed < 1

Editor
------
	- Fix selecting an entity/position while panning the camera with Space
	- Fix not being able to tab into play because a hidden control can still have keyboard focus
	- Fix `[angle]` control indicator line when set to `radians`
	- Fix crash when undoing deleted camera node
	- Fix not being able to open wind/particle when editor panels are hidden
	- Fix F5 trying load nexus scripts in editor, locking the UI
	- Fix rotating prop by 1 degree increments (ctrl+shift) also changing layer
	- Fix tooltips and `var_info` path returned for nested arrays
	- Fix script variable changes lost when compiling or entering playing
	- Fix "Enable Attack" highlighted in trigger list when a "Max Special" trigger is selected
	- Fix colour picker sliders showing the wrong values for certain colours
	- Prevent Alt+Click drawing tiles while `GVB_LEFT_CLICK` is cleared via script
	- Allow inserting a space into text fields while holding Space

Dustscript API
--------------
	- Fix not being able to disable script camera
	- Fix dropdowns for strings, non-sequential, or values not starting at 0
	- Fix spring blobs not triggering hit/hurt callbacks
	- Add :ref:`scene.save_checkpoint <method-scene-save_checkpoint>` overload that can use the `x` and `y` arguments
	- `editor_tab` will now return **"Wind"** and **"Particle"** instead of **""**
	  and **"Help"** when the wind and particle editors are open.
	- Added the :ref:`class-input_api` for direct mouse and keyboard access
	- Deprecated all :ref:`class-editor_api` keyboard methods - use the new input
	  API.
