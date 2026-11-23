---
id: flat-degree
title: The Arakelov degree of a flat frame function
kind: theorem
decl: GlobalTheory.CompanionTheory.Ar.Fl.flatDegree
module: Development.AutomorphicSpectrum.Proofs.GeometryProofs.FlatDegreeHolds
covers: 684
status: drafted
drafted_by: writer@claude
---
This theorem proves `FlatDegree`: if a frame function is flat in the complex uniformization, then its family of log norms is adelic, and its Arakelov degree is a constant built from $L'(1,\chi)/L(1,\chi)$ for the Kronecker character of $\mathbb{Q}(\sqrt{-d})$. Its statement form is [`FlatDegree_holds`](/entry/flat-degree-holds/). Its users are [`goodTower_and_volume`](/entry/good-tower-and-volume/) and `degree_of_flatOnModel`, below [`topCovolSlim2_use_alt_alt`](/proof/literature/).

## Statement

Let $E$ be a CM field with a host datum $H$: a prime $d \equiv 7 \pmod{16}$, an element $\sqrt{-d} \in \mathcal{O}_E$ and a complex root $\mathrm{rt}_0$ of $-d$. Let $D$ be an $\mathcal{O}_E$-lattice with a unimodular alternating form of signature $(p, q)$, and $X^\circ$ the moduli space of type $D$ at a level $l$. Let $F \subset \mathbb{C}$ be a coefficient field, $U$ a set of points of $X^\circ_F$, and $\tau \colon E \to \mathbb{C}$ with $\tau(\sqrt{-d}) = \mathrm{rt}_0$.

A *frame function* $\varphi$ gives, for a point $y$ of $X^\circ_F$ over a field $F'$, $p$ tangent vectors $v$ of type $\tau$ and $q$ vectors $w$ of type $\bar\tau$, a value $\varphi(y, v, w) \in F'$. A family of log norms $N$ on $F$ is a real number $N_\infty(s)$ for each $s \colon F \to \mathbb{C}$ and $N_\ell(\kappa)$ for each prime $\ell$ and $\kappa \colon F \to \mathbb{C}_\ell$. It is *adelic* if $N_\ell \ne 0$ for only finitely many $\ell$, and
$$\deg N = -\frac{1}{[F:\mathbb{Q}]}\Bigl(\sum_s N_\infty(s) + \sum_\ell \sum_\kappa N_\ell(\kappa)\Bigr).$$

**Theorem.** Let $\chi$ be a Dirichlet character mod $d$ with $\chi(n) = \bigl(\tfrac{-d}{n}\bigr)$ for odd $n$. Let $\mathrm{ty}$ be a list of embeddings $E \to \mathbb{C}$ in which each $\tau'$ appears $p$ times if $\tau'(\sqrt{-d}) = \mathrm{rt}_0$ and $q$ times otherwise. Suppose:

1. (`IsFlatGen`) the $i$-th uniformized component lies in $U$; $\varphi$ is nonzero, of weight $\det A / \det B$ under a change of frame, and compatible with field maps; and for some $\mathcal{O}_E$-independent vectors $e_1, \dots, e_{p+q}$ of its lattice, $\varphi$ times the period determinant of the frame is a constant $\rho$;
2. (`HasNorms`) $N_\infty(s) = \log|\varphi| + \tfrac12(\log|\det\Gamma| - \log|\det\Delta|)$ at each framed complex point, with $\Gamma, \Delta$ the Gram matrices of $v, w$; and $N_\ell(\kappa) + q(\log|\mathfrak{D}_E|_\kappa - \log|d|_\ell) = \log|\varphi|_\ell$ at integral frames over discrete valuation rings.

Then $N$ is adelic and
$$\deg N = \frac{p-q}{2}\,\mathrm{Re}\Bigl(\gamma + \log\frac{2\pi}{\mathrm{rd}(E)} - \frac{L'(1,\chi)}{L(1,\chi)}\Bigr) + q\bigl(\log d - \log \mathrm{rd}(E)\bigr),$$
where $\mathrm{rd}(E) = |\mathrm{disc}\,E|^{1/[E:\mathbb{Q}]}$ and $\gamma$ is Euler's constant.

## Proof

1. `T.chowla_selberg_period` gives, for $\pm\mathrm{rt}_0$, a CM elliptic curve with a period $z_\pm \ne 0$ whose mean log Lie norm is $-x$, with $x = \gamma + \log(2\pi/\sqrt d) - L'(1,\chi)/L(1,\chi)$. We have not compared it with the published Chowla-Selberg formula.
2. `T.frame_function_cm_value` gives a number field $k \supseteq F$ and $r \in k^\times$ with $r z_+^p = \rho z_-^q$.
3. `T.frame_function_cm_number_field` computes $N_\infty(s)$ from $\log|s(r)|$, the Lie norms and the Gram determinant of $e$.
4. `T.frame_function_cm_height` gives for each $\ell$ an element $t_\ell \in E$ that fixes $N_\ell$ and is a unit at $\ell$ when $e$ is a local basis there. This holds at almost all $\ell$ (`T.gram_det_ne_zero_local_basis_cofinite`).
5. `T.hermitian_metric_log_norm_formula` sums the local terms. `logNorms_ext_deg_isAdelic` shows that the extension from $F$ to $k$ keeps the degree and adelicity.

Local lemmas such as `flatDegree_mean_ext` do the bookkeeping. The degree does not depend on $i$, $U$ or $\tau$.

## In the Lean code

The theorem is in [FlatDegreeHolds.lean](lean:Development/AutomorphicSpectrum/Proofs/GeometryProofs/FlatDegreeHolds.lean#L60). `FlatDegree` is in [FlatDegree.lean](lean:Development/AutomorphicSpectrum/Statements/GeometryStatements/FlatDegree.lean#L12) and `IsFlatGen` and `HasNorms` in [IsConstMul.lean](lean:Development/AutomorphicSpectrum/Definitions/GlobalGeometry/IsConstMul.lean#L52). We have not opened the proofs of the lemmas in steps 1 to 5. The Lean form writes $2\log\sqrt d$ for $\log d$.
