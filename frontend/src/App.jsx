import { useEffect, useState } from "react";
import "./App.css";

const API = "http://localhost:8000/api";

export default function App() {
  const [propostas, setPropostas] = useState([]);
  const [cursos, setCursos] = useState([]);
  const [tecnologias, setTecnologias] = useState([]);
  const [filtros, setFiltros] = useState({ pesquisa: "", curso: "", tecnologia: "", orientador: "" });
  const [aCarregar, setACarregar] = useState(true);
  const [erro, setErro] = useState(null);

  // Opções dos filtros: cursos vêm de /api/cursos/, tecnologias da lista completa de propostas
  useEffect(() => {
    fetch(`${API}/cursos/`)
      .then((r) => r.json())
      .then(setCursos)
      .catch(() => {});
    fetch(`${API}/propostas/`)
      .then((r) => r.json())
      .then((lista) => setTecnologias([...new Set(lista.flatMap((p) => p.tecnologias))].sort()))
      .catch(() => {});
  }, []);

  // Lista filtrada: os filtros vão para o backend como query string
  useEffect(() => {
    const params = new URLSearchParams();
    Object.entries(filtros).forEach(([chave, valor]) => valor && params.set(chave, valor));
    const controlador = new AbortController();

    setACarregar(true);
    fetch(`${API}/propostas/?${params}`, { signal: controlador.signal })
      .then((r) => {
        if (!r.ok) throw new Error(`Erro ${r.status}`);
        return r.json();
      })
      .then((dados) => {
        setPropostas(dados);
        setErro(null);
      })
      .catch((e) => {
        if (e.name !== "AbortError") setErro(e.message);
      })
      .finally(() => setACarregar(false));

    return () => controlador.abort();
  }, [filtros]);

  const alterar = (campo) => (e) => setFiltros((f) => ({ ...f, [campo]: e.target.value }));

  return (
    <main className="pagina">
      <header>
        <h1>Propostas de TFC</h1>
        <p className="sub">Propostas disponíveis para candidatura</p>
      </header>

      <section className="filtros" aria-label="Filtros">
        <input type="search" placeholder="Pesquisar no título ou descrição" value={filtros.pesquisa} onChange={alterar("pesquisa")} />
        <select value={filtros.curso} onChange={alterar("curso")}>
          <option value="">Todos os cursos</option>
          {cursos.map((c) => (
            <option key={c.id} value={c.codigo}>{c.codigo}</option>
          ))}
        </select>
        <select value={filtros.tecnologia} onChange={alterar("tecnologia")}>
          <option value="">Todas as tecnologias</option>
          {tecnologias.map((t) => (
            <option key={t} value={t}>{t}</option>
          ))}
        </select>
        <input type="search" placeholder="Orientador" value={filtros.orientador} onChange={alterar("orientador")} />
      </section>

      {erro && (
        <p className="erro" role="alert">
          Não foi possível obter as propostas ({erro}). Confirma que o backend está a correr em {API.replace("/api", "")}.
        </p>
      )}
      {aCarregar && !erro && <p className="estado">A carregar…</p>}
      {!aCarregar && !erro && propostas.length === 0 && (
        <p className="estado">Nenhuma proposta com estes filtros. Se a lista está sempre vazia, corre o carregar_demo no backend.</p>
      )}

      {propostas.length > 0 && (
        <>
          <p className="contagem">{propostas.length} proposta{propostas.length !== 1 && "s"}</p>
          <ul className="lista">
            {propostas.map((p) => (
              <li key={p.id} className="proposta">
                <div className="topo">
                  <h2>
                    <span className="codigo">{p.codigo}</span> {p.titulo}
                  </h2>
                  <span className="candidaturas" title="Candidaturas na lista">
                    {p.numero_candidaturas} candidatura{p.numero_candidaturas !== 1 && "s"}
                  </span>
                </div>
                <p className="descricao">{p.descricao}</p>
                <dl className="meta">
                  <div><dt>Orientador</dt><dd>{p.orientador ?? "Por definir"}</dd></div>
                  <div><dt>Modalidade</dt><dd>{p.modalidade}</dd></div>
                  <div><dt>Cursos</dt><dd>{p.cursos.join(", ")}</dd></div>
                  {p.area_aplicacao && <div><dt>Área</dt><dd>{p.area_aplicacao}</dd></div>}
                </dl>
                <ul className="tecnologias">
                  {p.tecnologias.map((t) => (
                    <li key={t}>{t}</li>
                  ))}
                </ul>
              </li>
            ))}
          </ul>
        </>
      )}
    </main>
  );
}