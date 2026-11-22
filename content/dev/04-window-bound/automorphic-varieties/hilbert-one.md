---
id: hilbert-one
title: Level one Hilbert modular forms congruent to 1
kind: theorem
decl: GlobalTheory.HilbertThetaSeries.hilbertOne
module: Development.AutomorphicArithmetic.AutomorphicVarieties.GaussSumFiltrations.HasQOfSmallSubOne
covers: 580
status: drafted
drafted_by: writer@claude
---
This theorem proves `HilbertOne`: there are level one Hilbert modular forms in all weights divisible by $(p-1)p^N$ whose $q$-expansion is $p$-adically close to $1$. It does this from a theta series of a lattice of rank $2(p-1)$. For $F = \mathbb{Q}$ the Eisenstein series $E_{p-1}$, which is congruent to $1$ modulo $p$, has this role (Serre, *Formes modulaires et fonctions zêta p-adiques*, LNM 350, 1973). [`exists_hilbertModularForm_congr_one`](/entry/exists-hilbert-modular-form-congr-one/) is a second name for it.

## Statement

**Theorem** (`HilbertOne`). Let $F$ be totally real, $p$ an odd prime and $\iota \colon \overline{\mathbb{Q}}_p \to \mathbb{C}$ an isomorphism. There is $N$ such that for each $k > 0$ with $(p-1)p^N \mid k$ there is $\varphi$ with `IsHol k (fun _ => 0) 1 φ` and `HasExp φ k c₀ c`, where $\|\iota^{-1}(c_0(y)) - 1\| < 1$ for all $y$ and $\|\iota^{-1}(c(\mathfrak{m}))\| < 1$ for all $\mathfrak{m} \neq 0$.

We have not unfolded the norm on $\overline{\mathbb{Q}}_p$.

## Proof

For a function $f$ on $\mathbb{H}^n$, `Small ι r f` says that $f$ has a $q$-expansion with coefficients of norm at most $r$ after $\iota^{-1}$.

1. **A local generator of the different.** Choose $\delta \in F$ with $\operatorname{ord}_w \delta = -\operatorname{ord}_w \mathfrak{d}$ at each $w \mid p$ (`IsDel`).
2. **The seed.** `seed_exists` takes an even positive definite integer matrix $G$ of size $2(p-1)$ and an integer matrix $S$ with $S^{\mathsf T} G S = G$ and $1 + S + \dots + S^{p-1} = 0$, so $S$ is an isometry of order $p$ with no nonzero fixed vector. Also $\det G = t^2$ with $(-1)^{(p-1)/2} t \equiv 1 \pmod p$. The theta series $\theta$ = `th G oneL` (not unfolded) has weight $p - 1$. It is holomorphic, of moderate growth, and modular up to eighth roots of unity. For each $\gamma$ with $p$-integral entries, twisted by $\delta$, and with totally positive determinant (`InG`), $\theta|_{p-1}\gamma - 1$ is `Small` with $r = 1/p$ (`Seed`).
3. **Representatives.** A finite set $Y$ of finite ideles gives $\mathrm{GL}_2(\mathbb{A}_f) = \bigcup_{y \in Y} \mathrm{GL}_2(F)^+ \begin{pmatrix} y & 0 \\ 0 & 1\end{pmatrix} K$, with $K$ = `KLev F 2 1`.
4. **Averages.** For each $y \in Y$, `avg_pow` gives $N_y$ such that for each $M$ with $p^{N_y} \mid M$ there is a form $f_y$ of weight $(p-1)M$ (`Comp`). It is invariant under the stabilizer of the coset of $y$, and $f_y|\gamma - 1$ is `Small` with $r = 1/p$ for each $\gamma$ in `InG`. We have not unfolded its proof.
5. **Gluing.** Let $N = \max_y N_y$ and $k = (p-1)p^N m$. The forms $|y|^{k/2} f_y$ glue into a system $\Psi$ on $\mathrm{GL}_2(\mathbb{A}_f)$ (`Sys`). Since $p$ is odd, $k$ is even, so $\Psi$ lifts to an adelic form $\varphi$ with `IsHol k (fun _ => 0) 1 φ`.
6. **The congruence.** Each component $|y|^{-k/2}\Psi(y) - 1$ is `Small` with $r = 1/p$. So `hasQ_of_small_sub_one` gives a $q$-expansion $a_y$ with $\|\iota^{-1}(a_y(0)) - 1\| < 1$ and $\|\iota^{-1}(a_y(1))\| < 1$.
7. **The adelic expansion.** `exists_adelic_fourier_expansion_of_lift` gives `HasExp φ k c₀ c` with $c_0(y) = a_y(0)$, and for each $\mathfrak{m} \neq 0$ some $y$ with $c(\mathfrak{m}) = a_y(1)$.

## In the Lean code

The theorem is in [HasQOfSmallSubOne.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/GaussSumFiltrations/HasQOfSmallSubOne.lean#L33). `Small`, `Seed`, `Comp` and `Sys` are in [EvenPos.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/GaussSumFiltrations/EvenPos.lean#L74). Each lemma `GlobalTheory.T.*` is in a file of the same folder named after it.

- The hypothesis $k > 0$ of `HilbertOne` is not used ([line 47](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/GaussSumFiltrations/HasQOfSmallSubOne.lean#L47)).
- The proof gives every coefficient within $1/p$, but the statement keeps only the bound $< 1$.
