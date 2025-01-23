init -2 python:

    # The color of non-interactive text (深灰色，增强对比)
    custom_text = "#333333"  # 使用深灰色文本，确保在白色背景上清晰可见

    # Colors for buttons in various states
    custom_idle = "#2E3B4E"  # 深蓝色作为默认按钮背景
    custom_hover = "#FF4500" # 橙色用于悬停时按钮
    custom_disable = "#808080" # 灰色用于禁用按钮

    # Colors for reversed text buttons (selected list entries).
    custom_reverse_idle = "#000000D0"  # 黑色半透明背景，用于选中的按钮
    reverse_hover = "#FFA07A"          # 浅橙色，用于悬停时按钮的背景
    custom_reverse_text = "#FFFFFF"    # 白色文本，确保在深色背景上清晰

    # Colors for the scrollbar thumb.
    custom_scrollbar_idle = "#2E3B4E"  # 深蓝色滚动条，确保突出显示
    custom_scrollbar_hover = "#FF4500" # 橙色滚动条，悬停时突出显示

    # An image used as a separator pattern.
    custom_pattern = "images/pattern.png"

    # A displayable used for the background of everything.
    custom_background = "skin_background.png"

    # A displayable used for the background of the projects list.
    custom_projects_window = Null()

    # A displayable used the background of information boxes.
    custom_info_window = "#000000A0"  # 半透明黑色背景，确保信息框与背景区分开

    # Colors for the titles of information boxes.
    custom_error_color = "#FF6347"      # 错误信息，红色
    custom_info_color = "#333333"       # 信息文本颜色，深灰色，适合白色背景
    custom_interaction_color = "#FFD700" # 互动提示，金黄色
    custom_question_color = "#FFD700"   # 问题提示，金黄色

    # The color of input text.
    custom_input_color = "#333333"  # 深灰色输入文本，增强对比度

    # A displayable used for the background of windows
    # containing commands, preferences, and navigation info.
    custom_window = Null()