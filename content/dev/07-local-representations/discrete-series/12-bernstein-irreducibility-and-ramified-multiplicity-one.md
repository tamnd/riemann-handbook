---
title: Bernstein irreducibility and ramified multiplicity one
decls:
  - PositivityTheory.BernsteinRamification.narrowBern
  - PositivityTheory.BernsteinRamification.finSplit_of_geo
  - PositivityTheory.BernsteinRamification.Close.finSplit
  - PositivityTheory.BernsteinRamification.ramifiedMultiplicityOne_of_geometricFiltration
  - PositivityTheory.BernsteinRamification.Close.ramifiedMultiplicityOne
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Bernstein irreducibility and ramified multiplicity one

This section proves that a representation of $\mathrm{GL}_{a+b}$ over a $p$-adic field induced from two unitary characters of determinant type is irreducible, unless the two blocks have the same size and the same character. It then deduces two local facts for theta lifts between unitary groups: the existence of irreducible local quotients at the places outside the ramification set that split in $E$, and multiplicity one for local equivariant functionals at the ramified places. Both facts are inputs of [Theorem 2.6.4 of Volume 12](/entry/theorem-k-head2-of-mod/), which is used in the step [theta integrals agree and local matching](/step/theta-integrals-agree-and-local-matching-of-literature/).

Background: [smooth representations of p-adic groups](/learn/representations/#smooth-representations-of-p-adic-groups), [parabolic induction and the Jacquet module](/learn/representations/#parabolic-induction-and-the-jacquet-module), [[induction|JJP4JFH3C6]], [[irreducible representation|FX3NEFYFFN]], [[theta correspondence|ZBGT50BW0Z]], [[Weil representation|CD20HVR9V8]].

Let $k$ be a nonarchimedean local field. A character $\chi: k^\times \to \mathbb{C}^\times$ is smooth if its kernel is open, and unitary if $|\chi| = 1$. For $a \in \mathbb{N}$ write $\chi \circ \det_a$ for the character $g \mapsto \chi(\det g)$ of $\mathrm{GL}_a(k)$. For representations $\pi_1$ of $\mathrm{GL}_a(k)$ and $\pi_2$ of $\mathrm{GL}_b(k)$, $\pi_1 \times \pi_2$ is the smooth part of the induction of $\pi_1 \otimes \pi_2$, twisted by $\delta_P^{1/2}$, from the standard parabolic subgroup $P$ with Levi subgroup $\mathrm{GL}_a(k) \times \mathrm{GL}_b(k)$ to $\mathrm{GL}_{a+b}(k)$. A representation is irreducible if it has exactly two subrepresentations, $0$ and the whole space.

**Definition 3.12.1 (Geometric lemma).** For two ordered partitions $m$ and $m'$ of $n$, the geometric lemma for $k$ states: there is an enumeration $b_1, \dots, b_N$ of the matrices of natural numbers with row sums $|m_i|$ and column sums $|m'_j|$ such that, for every smooth representation $\rho$ of the Levi subgroup $M_m$, the Jacquet module of $\operatorname{Ind}_{P_m}(\rho)$ along $P_{m'}$ has a chain of subrepresentations $0 = S_0 \le \dots \le S_N$ equal to the whole module at the top, and $S_{t}/S_{t-1}$ is isomorphic to the cell functor of $b_t$ applied to $\rho$ (a Jacquet module for a smaller Levi subgroup, followed by conjugation and induction). The geometric lemma is this statement for every nonarchimedean local field $k$.

**Theorem 3.12.2 (Bernstein).** Assume the geometric lemma. Let $k$ be a nonarchimedean local field, $a, b \in \mathbb{N}$, and $\chi_1, \chi_2$ smooth unitary characters of $k^\times$ with $a \ne b$ or $\chi_1 \ne \chi_2$. Then $(\chi_1 \circ \det_a) \times (\chi_2 \circ \det_b)$ is irreducible.

Lean: `PositivityTheory.BernsteinRamification.narrowBern`

This is a case of Bernstein's theorem that $\sigma_1 \times \sigma_2$ is irreducible for irreducible unitary $\sigma_1, \sigma_2$ (Bernstein 1984, see the notes below). The geometric lemma is Bernstein-Zelevinsky 1977, Geometric Lemma 2.12.

*Proof.* Let $I = (\chi_1 \circ \det_a) \times (\chi_2 \circ \det_b)$ and $\sigma = \chi_1 \circ \det_a \otimes \chi_2 \circ \det_b$. The proof uses the following separate results, whose statements we read. First, $I$ is nonzero, admissible and unitarizable, and $\mathrm{GL}_{a+b}(k)$ has small compact open subgroups. Second, an admissible unitarizable representation of such a group is semisimple: every subrepresentation $W$ has a complement $W'$. Third, from the geometric lemma and the hypothesis on $(a, \chi_1)$ and $(b, \chi_2)$: for any two intertwining maps $\phi, \psi$ from the Jacquet module of $I$ along $P$ to $\sigma$, either $\phi = 0$ or $\psi$ is a multiple of $\phi$. Fourth, if $I = W \oplus W'$ with $W \ne 0$ and $W' \ne 0$, then the conclusion of the third result fails.

Let $W$ be a subrepresentation and $W'$ a complement. Assume $W \ne 0$ and $W \ne I$. Then $W' \ne 0$, since a complement of $0$ is $I$ and the complement of $W$ is $W'$. The fourth result contradicts the third. So the subrepresentations of $I$ are $0$ and $I$, and $I \ne 0$. $\square$

**Definition 3.12.3 (Local data at a place).** The global setting is that of the theta lift in [Theorem 2.6.4 of Volume 12](/entry/theorem-k-head2-of-mod/): number fields $F \subseteq E$, an $F$-automorphism $\sigma$ of $E$, a base $B$, a geometry $G$ with dimension indices $a, a'$ and integers $p, q$, characters $X$ with a finite ramification set $T$, and two Weil representations $\omega$, $\omega'$. Local finite maps at a finite place $v$ are a space $\Pi_v$ and linear maps $p_v$, $p'_v$ from the Schwartz-Bruhat spaces of the two Weil models at $v$ to $\Pi_v$. They are good at $v$ if:

1. $p_v$ and $p'_v$ are onto;
2. they vanish on the augmentation subspaces of $\omega$ and $\omega'$ at $v$;
3. they are compatible with the action of the local unitary group $U(W)(F_v)$: if $p_v\varphi = p'_v\varphi'$, then $p_v(h\varphi) = p'_v(h\varphi')$;
4. $\Pi_v \ne 0$, and $\Pi_v$ has no subspaces stable under this action other than $0$ and $\Pi_v$;
5. if $v \notin T$, the two vacuum vectors have the same nonzero image;
6. if $v \in T$ and $v$ is in the distinguished set of $B$, a zeta condition holds.

**Theorem 3.12.4 (Split places).** Assume the geometric lemma. For all $F, E, \sigma, B, a, a', G, X, \omega, \omega'$ that form a matched triple, and for every finite place $v \notin T$ such that $E$ has an $F$-embedding into $F_v$, there are local finite maps that are good at $v$.

Lean: `PositivityTheory.BernsteinRamification.finSplit_of_geo`

*Proof.* Apply Bernstein's theorem, and then a separate theorem that builds the good local maps at split places from seven inputs: irreducibility of the induced representations $\operatorname{Ind}(\alpha, \beta)$ of $\mathrm{GL}_{a+a'}$ for unitary smooth $\alpha, \beta$ and $a' < a$, which follows from Bernstein's theorem because $a \ne a'$; the unramified maps built from it; and five facts on Iwasawa vanishing, the split place dictionary, uniqueness of the action, characters at split places and integers of completions. We did not open the proofs of these inputs. $\square$

**Theorem 3.12.5 (Split places, closed form).** For all data as in the last theorem, and every finite place $v \notin T$ such that $E$ has an $F$-embedding into $F_v$, there are local finite maps that are good at $v$.

Lean: `PositivityTheory.BernsteinRamification.Close.finSplit`

*Proof.* The geometric lemma is a theorem. Apply the last theorem. $\square$

**Theorem 3.12.6 (Ramified multiplicity one).** Assume the geometric lemma. Let $(G, X, \omega, \omega')$ and $(G_1, X, \omega_1, \omega'_1)$ be matched with local maps $R, R_f$ and $R_1, R_{f,1}$, where $G$ has dimensions $(a, a')$ and $G_1$ has dimensions $(a_1, a'_1)$. Assume a step type: either $a_1 = a$, $a'_1 + 2 = a'$, $G_1$ has the same $p$ as $G$ and one less $q$, $\chi = \beta$ and $r = a/2$; or $a_1 + 2 = a$, $a'_1 = a'$, $G_1$ has one less $p$ and the same $q$, $\chi = \alpha$ and $r = a'/2$, where $\alpha, \beta$ are the two characters of $X$. Let $H'$ be a plane adapted to the skew-hermitian spaces of $G$ and $G_1$ at indices $i_0, i_1$. Let $v \in T$, and let $\lambda, \lambda'$ be finite local equivariant maps at $v$ for $(\omega, \omega_1, H', \chi, r)$ with respect to $p_v$ and $p_{1,v}$. If $\lambda \ne 0$, then $\lambda' = c\lambda$ for some $c \in \mathbb{C}$.

Lean: `PositivityTheory.BernsteinRamification.ramifiedMultiplicityOne_of_geometricFiltration`

*Proof.* By Bernstein's theorem, apply the multiplicity one theorem for the ramified places, which takes the irreducibility of the representations $(\chi_1 \circ \det_a) \times (\chi_2 \circ \det_b)$ as its hypothesis. That proof runs as follows. Let $t$ be the local datum of $B$ at $v$. By the condition of being good at $v$, each element $h$ of the local unitary group of $G_1$ acts on $\Pi_{1,v}$ by a linear map $\tau(h)$ with $\tau(h)\,p_{1,v}\varphi = p_{1,v}(h\varphi)$. This is well defined because $p_{1,v}$ is onto and compatible with the action, and $\tau(1) = 1$. $\Pi_{1,v}$ has countable dimension, as the image of a Schwartz-Bruhat space over a local field, and it is irreducible under $\tau$. Each $\lambda$ as above gives an equivariant functional $\lambda \circ p_v$ for $\omega$ and an equivariant functional $\lambda \circ p'_v$ for $\omega'$. Choose $x$ with $\lambda(x) \ne 0$. In each step type, apply a separate theorem on multiplicity one for pairs at ramified places, with the Hecke character $\beta/\alpha$ or $\alpha/\beta$ and the ramification of the character at $v$. In the first step type it gives $c$ with $\lambda' \circ p_v = c\,\lambda \circ p_v$, and since $p_v$ is onto, $\lambda' = c\lambda$. The second step type is the same with $\omega'$ and $p'_v$. $\square$

**Theorem 3.12.7 (Ramified multiplicity one, closed form).** With the data and hypotheses of the last theorem, without the geometric lemma as a hypothesis, $\lambda' = c\lambda$ for some $c \in \mathbb{C}$.

Lean: `PositivityTheory.BernsteinRamification.Close.ramifiedMultiplicityOne`

*Proof.* The geometric lemma is a theorem. Apply the last theorem. $\square$

**Remark 3.12.8 (Formalization).** The hypothesis of Bernstein's theorem has three definitions with the same body: `NarrowBern` ([RamifiedMultiplicityOneOfGeometricFiltration.lean](lean:Development/WeilBound/CoreStatements/TemperedRepresentationTheory/BernsteinNarrowness/RamifiedMultiplicityOneOfGeometricFiltration.lean#L15)), and two definitions named `Narrow` ([KCoinvOfNarrow.lean](lean:Development/AutomorphicSpectrum/Proofs/BlockDecomposition/KCoinvOfNarrow.lean#L13), [LocalMultiplicityOneIrreducibleGL.lean](lean:Development/AutomorphicSpectrum/Proofs/BlockDecomposition/LocalMultiplicityOneIrreducibleGL.lean#L14)). The closed forms only discharge the geometric lemma, and the file repeats this for six results ([RamifiedMultiplicityOne.lean](lean:Development/WeilBound/CoreStatements/TemperedRepresentationTheory/BernsteinNarrowness/BernsteinClosure/RamifiedMultiplicityOne.lean#L6)). The geometric lemma has two proofs under two names ([Imports.lean](lean:Development/WeilBound/CoreStatements/TemperedRepresentationTheory/GeometricSplitting/Imports.lean#L5), [GeometricLemmaFiltrationHolds.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/GeometricLemmaFiltrationHolds.lean#L6)). The name `FinSplit` also denotes unrelated objects elsewhere in the code. We did not open the proofs of admissibility, unitarizability, semisimplicity, the Jacquet module bound, the non-scalar lemma, the seven inputs at split places, the multiplicity one theorem for pairs, or the geometric lemma. We did not unfold matched triples, adapted planes, the augmentation subspaces, the zeta condition or the finite local equivariant maps.

## Notes and references

The volume and Haar measure computations of the first three sections are explicit forms of the integral formula for the Cartan decomposition; see [Haar measure](/learn/analysis/#haar-measure) and [real reductive groups](/learn/real-groups/#real-reductive-groups). The discrete series, its Harish-Chandra parameter, the formal degree and the lowest $K$-type are in [discrete series and formal degrees](/learn/real-groups/#discrete-series-and-formal-degrees) and [discrete series](/learn/representations/#discrete-series). The decay of matrix coefficients is in [asymptotics of matrix coefficients](/learn/real-groups/#asymptotics-of-matrix-coefficients). Theta functions on tori are in [theta functions on complex tori](/learn/theta-functions-cm/#theta-functions-on-complex-tori). Parabolic induction and the geometric lemma for $p$-adic groups are in [parabolic induction and the Jacquet module](/learn/representations/#parabolic-induction-and-the-jacquet-module).

- S. Helgason, *Groups and Geometric Analysis*, Academic Press 1984, Chapter I, §5, for the integral formula of $G = K\exp(\mathfrak{p})$.
- Harish-Chandra, *Discrete series for semisimple Lie groups II*, Acta Math. 116 (1966) 1-111, for the classification of the discrete series by regular integral parameters and the formal degree.
- H. Hecht and W. Schmid, *A proof of Blattner's conjecture*, Invent. Math. 31 (1975) 129-154, for the lowest $K$-type.
- W. Schmid, *$L^2$-cohomology and the discrete series*, Ann. of Math. 103 (1976) 375-394, and M. Atiyah and W. Schmid, *A geometric construction of the discrete series for semisimple Lie groups*, Invent. Math. 42 (1977) 1-62, for the realization by Dirac type operators.
- A. W. Knapp, *Representation Theory of Semisimple Groups: An Overview Based on Examples*, Princeton 1986, Chapters VIII, IX and XII, for asymptotics of matrix coefficients and the discrete series.
- I. N. Bernstein and A. V. Zelevinsky, *Induced representations of reductive p-adic groups. I*, Ann. Sci. ENS 10 (1977) 441-472, for the geometric lemma.
- I. N. Bernstein, *P-invariant distributions on GL(N) and the classification of unitary representations of GL(N) (non-Archimedean case)*, Lecture Notes in Math. 1041 (1984) 50-102, for the irreducibility of unitary parabolic induction for $\mathrm{GL}_n$.
