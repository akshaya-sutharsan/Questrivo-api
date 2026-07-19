from flask import Flask, jsonify
from flasgger import Swagger
from app.config import Config
from app.extensions import db, jwt, cors


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    swagger = Swagger(app, template={
        "swagger": "2.0",
        "info": {
            "title": "AI Exam Generator API",
            "description": "API documentation for the AI Exam Generator backend",
            "version": "1.0.0"
        },
        "schemes": ["http", "https"],
        "securityDefinitions": {
            "Bearer": {
                "type": "apiKey",
                "name": "Authorization",
                "in": "header"
            }
        }
    }, config={
        "headers": [],
        "specs": [{
            "endpoint": "apispec",
            "route": "/docs/apispec.json",
            "rule_filter": lambda rule: True,
            "model_filter": lambda tag: True,
        }],
        "static_url_path": "/flasgger_static",
        "swagger_ui": True,
        "specs_route": "/docs/",
    })

    @app.get('/')
    def index():
        return jsonify({
            "message": "AI Exam Generator API is running",
            "docs": "/docs"
        }), 200

    @app.get('/health')
    def health_check():
        return jsonify({"status": "ok"}), 200

    db.init_app(app)
    jwt.init_app(app)
    cors.init_app(app)

    from app.routes.auth_routes import auth_bp
    from app.routes.teacher_routes import teacher_bp
    from app.routes.student_routes import student_bp
    from app.routes.subject_routes import subject_bp
    from app.routes.syllabus_routes import syllabus_bp
    from app.routes.lesson_routes import lesson_bp
    from app.routes.exam_routes import exam_bp
    from app.routes.question_routes import question_bp
    from app.routes.marking_scheme_routes import marking_scheme_bp
    from app.routes.quiz_routes import quiz_bp
    from app.routes.progress_routes import progress_bp
    from app.routes.ai_routes import ai_bp

    app.register_blueprint(auth_bp, url_prefix="/api/auth")
    app.register_blueprint(teacher_bp, url_prefix="/api/teachers")
    app.register_blueprint(student_bp, url_prefix="/api/students")
    app.register_blueprint(subject_bp, url_prefix="/api/subjects")
    app.register_blueprint(syllabus_bp, url_prefix="/api/syllabus")
    app.register_blueprint(lesson_bp, url_prefix="/api/lessons")
    app.register_blueprint(exam_bp, url_prefix="/api/exams")
    app.register_blueprint(question_bp, url_prefix="/api/questions")
    app.register_blueprint(marking_scheme_bp, url_prefix="/api/marking-schemes")
    app.register_blueprint(quiz_bp, url_prefix="/api/quizzes")
    app.register_blueprint(progress_bp, url_prefix="/api/progress")
    app.register_blueprint(ai_bp, url_prefix="/api/ai")

    with app.app_context():
        db.create_all()

    return app
