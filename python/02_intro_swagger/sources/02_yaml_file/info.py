"""
schema:
  $ref: '#/definitions/Cursor_lists'

definitions:
  Lists:
    type: object
    properties:
      created_at:
        type: string
      slug:
        type: string
      name:
        type: string
      description:
        type: string
      mode:
        type: string
      following:
        type: boolean
      user:
        $ref: '#/definitions/Users'
      member_count:
        type: integer
      id_str:
        type: string
      subscriber_count:
        type: integer
      id:
        type: integer
      uri:
        type: string

  Cursor_lists:
    type: object
    properties:
      previous_cursor:
        type: integer
      lists:
        type: array
        items:
          $ref: '#/definitions/Lists'
      previous_cursor_str:
        type: string
      next_cursor:
        type: integer
      next_cursor_str:
        type: string

"""
