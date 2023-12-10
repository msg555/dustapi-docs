22.7.1
======

Tools
-----
  - Add debug option to visualise dustblock clear regions for attacks and while falling

Editor
------
  - Add unique colours for some z triggers.
  - Add ability to overwriting everything with the dust/spike tool while holding Shift.
  - Changing layer with Ctrl+scroll while using the tile tool.
  - Fix colour picker hex input visibility.
  - Added zCamera trigger

Dustscript API
--------------
  - Fix :ref:`destroyed<method-entity-destroyed>` not being set for quils, hitboxes, and AI controllers.
  - Add :ref:`hitbox.triggered_outcome()<method-hitbox-triggered_outcome>`
  - Add filth type APIs

    - :ref:`controllable.filth_type<method-controllable-filth_type>`
    - :ref:`controllable.emitter_filth_type<method-controllable-emitter_filth_type>`
    - :ref:`controllable.attack_filth_type<method-dustman-attack_filth_type>`
    - `Example usage <https://gist.github.com/cmann1/c6df5a83490b2925a5749f701b1c049e>`_

  - Add :ref:`filth_ball<class-filth_ball>` class

    - `Example usage <https://gist.github.com/cmann1/3f1986ad8db25f153f893e62e409f5e8>`__

  - Add API to manipulate camera position and path behavior

    - `Example usage <https://gist.github.com/cmann1/257c34beb78ca4237abd57867bea34c0>`__

  - Add :ref:`camera_node<class-camera_node>` class

    - `Example usage <https://gist.github.com/cmann1/5c5d5e24b66e4d8f1feb2107460c0fa0>`__

  - Add new :code:`TYPE` options to :code:`entity` annotations to allow
    controlling the kind of entities that can be selected. See
    :ref:`trigger_base<class-trigger_base>` documentation.

  - Add methods to enable/disable :ref:`jump<method-scene-jump_enabled>`,
    :ref:`attack<method-scene-attack_enabled>`,
    :ref:`dash<method-scene-dash_enabled>`,
    and :ref:`special<method-scene-special_enabled>`

  - Add :ref:`dustman.dustblock_clear_speed()<method-dustman-dustblock_clear_speed>` 
    and :ref:`dustman.dustblock_clear_rect()<method-dustman-dustblock_clear_rect>`

  - Add :ref:`scene.clear_ghosts()<method-scene-clear_ghosts>`

  - Add :ref:`scene.user_id()<method-scene-user_id>`,
    :ref:`scene.player_user_id()<method-scene-player_user_id>`,
    and :ref:`replay_username()<method-scene-replay_username>`.
