---
title: Presentations of framed deformation rings
decls:
  - UpperTheory.V.Alg.lemmaP
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Presentations of framed deformation rings

This section constructs the graded rings to which the length bound of Section 6.12 is applied. A residual [[representation|WYGRXCG2RN]] $\bar\rho$ of a profinite group $\Gamma$ preserves a bilinear form up to scalars and a grading by an abelian group $X$. We frame its deformations at finitely many local groups and impose local conditions at others. The theorem gives the universal framed deformation ring a graded presentation over a base $B$: in weight $j$, the number of new variables is the dimension of a framed $H^1$ of the weight $j$ part of the adjoint representation, and the number of relations is the dimension of a framed obstruction group. It is used by [Theorem 8.1.6 of Volume 9](/entry/vwin-of-hypotheses-h-e-alt/), below [VWin](/step/vwin-def/), together with the length bound [Theorem 6.12.8](/entry/main-holds/).

### Forms, weights and lifts

In this section $\mathcal{O}$ is a [[Noetherian|0670T59HGE]] [[local ring|MZ02BKPHJA]], complete for its maximal ideal, with a finite residue field $k$ of characteristic $l \ne 2$. A *coefficient ring* is an $\mathcal{O}$-algebra $R$ that is a complete Noetherian local ring with $\mathcal{O} \to R$ local and with residue field $k$, as in condition 1 of Definition 6.11.1. Let $\iota$ be a finite set and $X$ a free abelian group of finite rank, with a weight function $w : \iota \to X$.

**Definition 6.13.1 (Form data).** A *form datum* consists of an invertible matrix $J \in M_\iota(\mathcal{O})$ with $J^{\mathrm{T}} = \pm J$, a function $\operatorname{blk} : \iota \to \kappa$ to a set of blocks with an involution $\sigma$ of $\kappa$, and an element $c \in X$, such that $J_{ab} \ne 0$ implies $\operatorname{blk}(b) = \sigma(\operatorname{blk}(a))$ and $w(a) + w(b) = c$.

Lean: `UpperTheory.V.Alg.FormData`.

For a coefficient ring $R$, let $\mathfrak{g}_R$ be the set of block diagonal $Y \in M_\iota(R)$ with $Y^{\mathrm{T}} J + J Y = 0$, and let $\mathfrak{g}_{R, j}$ be the set of $Y \in \mathfrak{g}_R$ with $Y_{ab} = 0$ unless $w(a) - w(b) = j$. Let $H(R)$ be the group of block diagonal $h$ with $h^{\mathrm{T}} J h = J$ and $h \equiv 1$ modulo $\mathfrak{m}_R$.

Lean: `UpperTheory.V.Alg.FormData.g`, `UpperTheory.V.Alg.FormData.gw`, `UpperTheory.V.Alg.FormData.HH`.

**Definition 6.13.2 (Normalised representation).** A homomorphism $\rho : \Gamma \to M_\iota(R)$ is *normalised* if for each $g$ there is $\nu \in R$ with $\rho(g)^{\mathrm{T}} J \rho(g) = \nu J$, if there is a homomorphism $\pi : \Gamma \to \operatorname{Perm}(\kappa)$ with $\operatorname{blk}(a) = \pi(g)(\operatorname{blk}(b))$ whenever $\rho(g)_{ab} \ne 0$, and if $\rho(g)_{ab} = 0$ whenever $w(a) \ne w(b)$. Conjugation by $\rho$ then preserves each $\mathfrak{g}_{R,j}$; we write $\operatorname{ad}_j \rho$ for it.

Lean: `UpperTheory.V.Alg.FormData.Normalises`, `UpperTheory.V.Alg.FormData.adRep`.

Fix a topological group $\Gamma$ and a normalised $\bar\rho : \Gamma \to M_\iota(k)$. A *lift* of $\bar\rho$ to $R$ is a homomorphism $r : \Gamma \to M_\iota(R)$ whose entries are continuous for the $\mathfrak{m}_R$-adic topology and which reduces to $\bar\rho$. A *condition* is a property of lifts to all coefficient rings. Fix a lift $r_0$ of $\bar\rho$ to $\mathcal{O}$ that is normalised. A lift $r$ is *in $H$* if $r(g) r_0(g)^{-1} \in H(R)$ for all $g$. For $t : X \to R^\times$, the *torus conjugate* of $r$ is the lift with entries $t(w(a) - w(b)) r(g)_{ab}$.

Lean: `UpperTheory.V.Alg.Lift`, `UpperTheory.V.Alg.Cond`, `UpperTheory.V.Alg.FormData.InH`, `UpperTheory.V.Alg.IsTorusConj`.

**Definition 6.13.3 (Local condition).** Let $N$ be a subgroup of $\Gamma$. A condition $L$ is a *local condition with tangent group $N$* if, on lifts in $H$:

1. for each lift $r$ to $R$ there is an ideal $I \subseteq R$ such that $r$ pushed along $f : R \to R'$ satisfies $L$ exactly when $f(I) = 0$;
2. $L$ is stable under conjugation by $H(R)$ and under torus conjugation by $t$ with $t \equiv 1$ modulo $\mathfrak{m}_R$;
3. for a surjection $p : R \to R'$ with $\mathfrak{m}_R \ker p = 0$, every lift to $R'$ with $L$ comes from a lift to $R$ with $L$;
4. for such $p$, and lifts $r_1$, $r_2$ to $R$ with the same image in $R'$ and with $r_1$ satisfying $L$, the lift $r_2$ satisfies $L$ exactly when $r_2 = r_1$ on $N$.

Lean: `UpperTheory.V.Alg.FormData.IsLocCond`.

Condition 3 is formal smoothness; condition 4 says that the tangent space is the cocycles that vanish on $N$.

### Frames and framed cohomology

**Definition 6.13.4 (Frame).** A *frame* for $\Gamma$ consists of a finite set $T$ with a base element $v_0$, a continuous homomorphism $\varphi_v : G_v \to \Gamma$ for each $v \in T$, a finite set $Q$, and for each $q \in Q$ a continuous homomorphism $\psi_q : G_q \to \Gamma$ and a subgroup $N_q \subseteq G_q$.

Lean: `UpperTheory.V.Alg.Frame`.

Let $M$ be a $k$-linear representation of $\Gamma$, and for $h : G \to M$ write $dh(s, t) = h(s) + s h(t) - h(st)$.

**Definition 6.13.5 (Framed cohomology).** The *framed first cohomology* $H^1_F(M)$ is the $k$-space of pairs $(a, y)$ with $a : \Gamma \to M$ a locally constant cocycle and $y : T \to M$, such that $a(\psi_q(N_q)) = 0$ for each $q$, $a(\varphi_v(s)) = \varphi_v(s) y_v - y_v$ for each $v$ and $s$, and $y_{v_0} = 0$. The *framed obstruction group* $\operatorname{Ob}_F(M)$ is the quotient of the space of triples $(c, (b_v), (b_q))$ of locally constant cochains, with $c$ a $2$-cocycle on $\Gamma$ whose restrictions along $\varphi_v$ and $\psi_q$ are $d b_v$ and $d b_q$, by the span of the triples
$$\bigl(dh, \ h \circ \varphi_v - (\varphi_v(\cdot) y_v - y_v), \ h \circ \psi_q - e_q\bigr),$$
where $h$ is locally constant, $y : T \to M$, and each $e_q$ is a locally constant cocycle on $G_q$ that vanishes on $N_q$.

Lean: `UpperTheory.V.Alg.dOne`, `UpperTheory.V.Alg.Frame.H1c`, `UpperTheory.V.Alg.Frame.framedTwoCocycles`, `UpperTheory.V.Alg.Frame.framedTwoCoboundaries`, `UpperTheory.V.Alg.Frame.Ob`.

In $H^1_F(M)$, the cocycle $a$ is a first-order deformation and $y_v$ a first-order change of the frame at $v$; the condition $y_{v_0} = 0$ removes the global conjugation. The group $\operatorname{Ob}_F(M)$ receives the obstructions to lifting framed deformations.

### Framed lifts and graded presentations

Let $B$ be a coefficient ring, and for each $v \in T$ let $\rho_v$ be a lift of $\bar\rho \circ \varphi_v$ to $B$ that is in $H$. Let $L_q$ be a condition on lifts of $\bar\rho \circ \psi_q$ for each $q$.

**Definition 6.13.6 (Framed lift).** A *framed lift* over a coefficient ring $R$ with a map $i : B \to R$ is a lift $r$ of $\bar\rho$ to $R$ in $H$, with $r \circ \psi_q$ satisfying $L_q$ for each $q$, together with $\alpha_v \in H(R)$ for $v \in T$ with $\alpha_{v_0} = 1$ and
$$r(\varphi_v(s)) \, \alpha_v = \alpha_v \, i(\rho_v(s)) \qquad (v \in T, \ s \in G_v).$$
It is *universal* if for every framed lift $(R', i', r', \alpha')$ there is a unique $\mathcal{O}$-algebra map $f : R \to R'$ with $f \circ i = i'$ that takes $r$ to $r'$ and $\alpha_v$ to $\alpha'_v$.

Lean: `UpperTheory.V.Alg.IsFramed`, `UpperTheory.V.Alg.IsUnivFramed`.

**Definition 6.13.7 (Weighted presentation).** A *weighted presentation* of $R$ is a finite set $\Sigma$ with weights $\operatorname{wt} : \Sigma \to X$ and a surjection $\pi : \mathcal{O}[[\Sigma]] \to R$ whose kernel is homogeneous for the weights. The weight $j$ part $R_j$ is the image of the weight $j$ series, and $z_u = \pi(X_u)$. Given a weighted presentation $(\Sigma_B, \pi_B)$ of $B$ and $i : B \to R$, a *relative presentation* is a weighted presentation $(\Sigma, \pi)$ of $R$ with $\Sigma = \Sigma_B \sqcup \tau$, weights on $\Sigma_B$ as before, $\pi$ extending $i \circ \pi_B$, and homogeneous series $f_u$ of weight $w_f(u)$ for $u$ in a finite set $\kappa'$, such that
$$\ker \pi = (\ker \pi_B)\, \mathcal{O}[[\Sigma]] + (f_u)_{u \in \kappa'}.$$

Lean: `UpperTheory.V.Alg.WPres`, `UpperTheory.V.Alg.WPres.part`, `UpperTheory.V.Alg.IsRelPres`.

We say that $\Gamma$ satisfies *the $\Phi$ condition for $l$* if each open subgroup has only finitely many continuous homomorphisms to $\mathbb{Z}/l$.

Lean: `UpperTheory.V.Alg.PhiCond`.

**Theorem 6.13.8 (Graded presentation of the framed deformation ring).** With $\mathcal{O}$ and $k$ as above, fix a form datum. Let $\Gamma$ be a compact, totally disconnected, Hausdorff topological group with the $\Phi$ condition for $l$. Let $\bar\rho$ be normalised, and $r_0$ a normalised lift to $\mathcal{O}$. Let $F$ be a frame with $\bar\rho(\psi_q(N_q)) = 1$, and for each $q$ let $L_q$ be a local condition for $r_0 \circ \psi_q$ with tangent group $N_q$, satisfied by $r_0 \circ \psi_q$. Assume that $\operatorname{Ob}_F(\operatorname{ad}_j \bar\rho)$ is finite-dimensional for each $j \in X$. Let $B$ be a coefficient ring with a weighted presentation whose variables map into $\mathfrak{m}_B$, and let $\rho_v$ be lifts in $H$ with $\rho_v(s)_{ab} \in B_{w(a) - w(b)}$. Then there are:

1. a universal framed lift $(R, i, r, \alpha)$;
2. a relative presentation of $R$ over $B$, with new variables $\tau$ and relations $(f_u)_{u \in \kappa'}$;

such that $r(g)_{ab}$ and $(\alpha_v)_{ab}$ lie in $R_{w(a) - w(b)}$, each new variable $z_t$ has weight $w(a) - w(b)$ and equals $r(s)_{ab} - r_0(s)_{ab}$ or $(\alpha_v - 1)_{ab}$ for some $a$, $b$, $s$ or $v$, and for every $j \in X$
$$\begin{aligned} \#\{t \in \tau : \operatorname{wt}(t) = j\} &= \dim_k H^1_F(\operatorname{ad}_j \bar\rho), \\ \#\{u \in \kappa' : w_f(u) = j\} &= \dim_k \operatorname{Ob}_F(\operatorname{ad}_j \bar\rho). \end{aligned}$$

Lean: `UpperTheory.V.Alg.lemmaP`, `UpperTheory.V.Alg.LemmaP`.

*Proof.* Since $l \ne 2$, $2$ is a unit in $\mathcal{O}$; this is the only use of $l \ne 2$.

1. *The universal ring.* The functor of framed lifts satisfies Schlessinger's conditions, since the $L_q$ are cut out by ideals and lift along small extensions. Its tangent space $H^1_F(\mathfrak{g}_k)$ is finite-dimensional by the $\Phi$ condition. So it is represented by a coefficient ring $R$ with a universal framed lift; compare Mazur, *Deforming Galois representations*, §1, for the unframed case.
2. *The grading.* Torus conjugation by $t : X \to R'^\times$ with $t \equiv 1$ acts on framed lifts, since the $L_q$ are stable under it and the $\rho_v$, $\bar\rho$ and $r_0$ respect the weights. This action gives a weighted presentation of $R$ in which $r(g)_{ab}$ and $(\alpha_v)_{ab}$ have weight $w(a) - w(b)$.
3. *The relative tangent space.* The relative cotangent space $\mathfrak{m}_R / (\mathfrak{m}_R^2 + \mathfrak{m}_B R + \mathfrak{m}_{\mathcal{O}} R)$ is dual to $H^1_F(\mathfrak{g}_k)$, and its weight $j$ part is dual to $H^1_F(\operatorname{ad}_j \bar\rho)$. It is spanned by the images of the entries $r(s)_{ab} - r_0(s)_{ab}$ and $(\alpha_v - 1)_{ab}$, each of weight $w(a) - w(b)$. Choose among them a homogeneous basis $(z_t)$.
4. *The relative presentation.* The variables of $B$ and the $z_t$ give a surjection $\mathcal{O}[[\Sigma_B \sqcup \tau]] \to R$ that extends $i \circ \pi_B$ and respects weights. Its kernel is generated by $\ker \pi_B$ and homogeneous relations $f_u$, which we choose minimal: their images in $\ker \pi / (\mathfrak{m} \ker \pi + \ker \pi_B)$ are linearly independent.
5. *The obstruction bound.* Lifting the universal framed lift to $\mathcal{O}[[\Sigma]] / \mathfrak{m} \ker \pi$ and measuring the failure of the homomorphism property by a framed $2$-cocycle gives an injective map, respecting weights, from the dual of the relation space to $\operatorname{Ob}_F(\mathfrak{g}_k)$. So the number of relations of weight $j$ is at most $\dim_k \operatorname{Ob}_F(\operatorname{ad}_j \bar\rho)$.
6. *Padding.* For $j$ not of the form $w(a) - w(b)$ the space $\mathfrak{g}_{k,j}$ is zero, so $\operatorname{Ob}_F(\operatorname{ad}_j \bar\rho) = 0$. For the finitely many other $j$, add zero relations of weight $j$ until the count is $\dim_k \operatorname{Ob}_F(\operatorname{ad}_j \bar\rho)$. Zero relations do not change the kernel. $\square$

**Remark 6.13.9 (Formalization).** The equality for the number of relations is reached by padding with zero relations, so it is not stronger than the inequality; the relation family of the result is `Sum.elim f fun _ => 0` ([LemmaP.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/CommutativeAlgebra/LemmaP.lean#L407)). The existence theorem `framed_univ` ends its hypotheses with a dummy argument `∀ (_ : Unit)` ([FramedUniv.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/CommutativeAlgebra/FramedUniv.lean#L299)), and the proof of the Theorem passes `()` to it ([LemmaP.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/CommutativeAlgebra/LemmaP.lean#L265)). The dimensions are `Module.finrank`, which is $0$ for an infinite-dimensional space, so finiteness of the obstruction groups is a hypothesis. Universality is stated only for coefficient rings in `Type`, the lowest universe.

## Notes and references

The chapter supplies inputs to results of Volume 3 in two groups. The first group is étale. The projective bundle formula in all ranks, [Lemma 5.5.3](/entry/pbf-all/), uses the rank two case and the induction step, and through them the Künneth formula for $\mathbb{G}_m$. The finiteness theorem for étale cohomology, [Theorem 3.7.1](/entry/etale-topology-top/), uses the finiteness of Picard torsion, which rests on the section on Kummer classes, and the relative cohomology objects of Section 6.7. The representation of clopen subschemes of fixed rank feeds [Theorem 5.1.4](/entry/exists-finite-etale-representing-clopen-subschemes/). The treatment differs from the classical one in three places. Cohomology is defined for spaces, by maps into one fixed injective resolution, so that covers and fibre products need no separate theory. The finiteness of Picard torsion avoids Jacobians and uses Selmer groups of function fields. The derived direct images of Section 6.7 are built by hand from injective sheaves.

The second group is coherent and algebraic. Sections 6.8 to 6.10 prove Grothendieck's finiteness theorem for coherent cohomology on proper schemes over a Noetherian ring, [Theorem 6.10.6](/entry/ground-theory-arith-scheme-coh-finite-h-of-is-proper/), which feeds [EveryCharacter](/step/every-character/), the place where the proof splits into its two large parts. The route is classical: Serre's computation on projective space, Chow's lemma, and Noetherian induction, with a comparison of Čech complexes in place of the Leray spectral sequence for the Chow map. Sections 6.11 to 6.13 give the commutative algebra of the deformation side. The length bound [Theorem 6.12.8](/entry/main-holds/) and the graded presentation [Theorem 6.13.8](/entry/lemma-p/) are used by [Theorem 8.1.6 of Volume 9](/entry/vwin-of-hypotheses-h-e-alt/) on the way to [VWin](/step/vwin-def/), and the length bound also by [Theorem 7.7.4 of Volume 9](/entry/abstract-count/).

- J. S. Milne, *Étale Cohomology*, Princeton University Press, 1980. Chapter I, §4 (étale morphisms); Chapter III, §1 (cohomology on the étale site) and Proposition 4.9 (Hilbert's Theorem 90); Chapter VI, §2 and §4 (proper and smooth base change), §10 (the projective bundle formula).
- A. Grothendieck et al., *SGA 4*, Exposé XIV (finiteness theorems), and *SGA 5*, Exposé VII (the projective bundle formula and Chern classes in étale cohomology).
- A. Grothendieck and J. Dieudonné, *EGA II*, Théorème 5.6.1 (Chow's lemma); *EGA III*$_1$, Théorème 3.2.1 (finiteness of coherent cohomology for proper morphisms).
- A. Grothendieck, *EGA IV*, 17.9.1 (étale morphisms and open immersions); and "Techniques de construction et théorèmes d'existence en géométrie algébrique IV: les schémas de Hilbert", Séminaire Bourbaki 221.
- R. Hartshorne, *Algebraic Geometry*, Springer, 1977. Chapter I, §6 (nonsingular curves and function fields); Chapter II, §5 and Theorem 5.17 (coherent sheaves and Serre's global generation theorem), Exercise 4.10 (Chow's lemma); Chapter III, Proposition 2.6, Lemma 2.10, Theorem 4.5, Theorems 5.1 and 5.2, Exercises 4.11 and 8.1 (cohomology of coherent sheaves, Čech cohomology, and cohomology of projective space).
- D. Mumford, *Abelian Varieties*, Oxford University Press, 1970. §4 (the $n$-torsion points of an abelian variety).
- S. Lang, *Algebra*, revised third edition, Springer, 2002. Chapter VI, §8 (Kummer theory), used in the Lemma on descent of Selmer classes.
- N. Spaltenstein, "Resolutions of unbounded complexes", *Compositio Math.* 65 (1988). K-injective complexes.
- J.-P. Serre, *Algèbre locale. Multiplicités*, Lecture Notes in Mathematics 11, Springer. Chapter IV (Koszul complexes and multiplicities).
- B. Mazur, "Deforming Galois representations", in *Galois Groups over* $\mathbb{Q}$, MSRI Publications 16, Springer, 1989. §1 (universal deformation rings).
- G. Böckle, "Deformations of Galois representations", in *Elliptic curves, Hilbert modular forms and Galois deformations*, Advanced Courses in Mathematics CRM Barcelona, Birkhäuser, 2013 (framed deformations and presentations).
