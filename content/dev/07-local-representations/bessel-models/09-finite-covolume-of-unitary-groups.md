---
title: Finite covolume of unitary groups
decls:
  - CompanionTheory.SWFin.finVol
  - CompanionTheory.SWFin.adelicCovolumeFinite
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Finite covolume of unitary groups

This section proves that the rational points of a unitary group of a nondegenerate Hermitian form over a CM field form a lattice of finite covolume in its adelic points. This is the case of unitary groups of the theorem of [[Borel and Harish-Chandra|3B451RD8AJ]] (Ann. of Math. 75 (1962)); see [quotients of finite volume](/learn/groups/#quotients-of-finite-volume). The global Bessel and Fourier-Jacobi periods of the theory are integrals over such quotients, and the theorem on [the finite volume of unitary groups](/entry/fin-vol-unitary-group/) restates the result of this section for the counting arguments of the Hermitian lattice volume. The proof reduces the adelic statement to an arithmetic one at the archimedean places, through lattices.

### Unitary groups over a CM field

Let $F$ be a number field and $E / F$ an extension of number fields with an $F$-automorphism $\sigma$ of $E$.

**Definition 6.9.1 (CM extension).** The pair $(E/F, \sigma)$ is a *CM extension* if $F$ is totally real, $E$ is totally complex, $[E : F] = 2$, and $\tau(\sigma(x)) = \overline{\tau(x)}$ for every embedding $\tau : E \to \mathbb{C}$ and every $x \in E$.

**Definition 6.9.2 (Unitary group).** Let $J$ be an $M \times M$ matrix over $E$ with $\sigma(J_{ba}) = J_{ab}$ for all $a, b$ and $\det J \neq 0$. For a commutative $F$-algebra $R$ let
$$U_J(R) = \{ g \in \mathrm{GL}_M(R \otimes_F E) : \sigma(g)^{\mathsf{T}} J g = J \},$$
where $\sigma$ acts on the second factor. The group $U_J(F)$ embeds diagonally in $U_J(\mathbb{A}_F)$, a locally compact group.

**Definition 6.9.3 (Finite volume).** We say that $U_J$ has *finite volume* if a Haar measure on $U_J(\mathbb{A}_F)$ exists and, for each Haar measure $\mu$, a [[fundamental domain|KNJA2NEZ9F]] for the left action of $U_J(F)$ on $U_J(\mathbb{A}_F)$ exists and every fundamental domain $\mathcal{F}$ has $\mu(\mathcal{F}) < \infty$.

See [adelic points and compact open subgroups](/learn/groups/#adelic-points-and-compact-open-subgroups) and [unitary groups](/learn/groups/#unitary-groups) for the background.

### The adelic statement

For the proof we use a basis-free form. Let $h$ be a nondegenerate Hermitian form on a finite-dimensional $E$-space $W$ with a basis $v$, and let $\mathrm{U}(h)$ be its unitary group over $F$. The Gram matrix of $h$ in $v$ defines the adelic group $U(\mathbb{A}_F)$, and $\mathrm{U}(h)$ embeds diagonally in it.

**Theorem 6.9.4 (Adelic covolume).** Let $F$ be totally real and $E/F$ a totally complex quadratic extension. For each nondegenerate Hermitian form $h$ on $W$, each basis $v$ of $W$ and each Haar measure $\mu$ on $U(\mathbb{A}_F)$, there is a fundamental domain $\mathcal{F}$ for the diagonal image of $\mathrm{U}(h)$ with $\mu(\mathcal{F}) < \infty$.

Lean: `CompanionTheory.SWFin.adelicCovolumeFinite`.

*Proof.* We use five proved inputs.

1. *Archimedean identification.* Let $U_\infty$ be the product over the complex places $w$ of $E$ of the unitary groups of the Gram matrices of $h$ at $w$. There is an isomorphism of topological groups $\psi$ from the infinite-adelic points $U(\mathbb{A}_{F,\infty})$ to $U_\infty$ that takes the archimedean part of the diagonal image of $\gamma \in \mathrm{U}(h)$ to the archimedean embedding $\iota_\infty(\gamma)$.
2. *Lattice dictionary.* There are a compact open subgroup $K$ of $U(\mathbb{A}_{F,f})$, an integer $D$ and a map $s \mapsto L(s)$ from $U(\mathbb{A}_{F,f})$ to lattices in $W$ such that each $L(s)$ is $D$-integral, $L(\gamma_f s) = \gamma \cdot L(s)$ for $\gamma \in \mathrm{U}(h)$, and $L(s) = L(s')$ if and only if $s^{-1} s' \in K$. A lattice is *$D$-integral* if $h$ takes integral values on it and its index in its dual is at most $D$.
3. *Finiteness of lattice classes.* For each $D$ there is a finite set $S_0$ of lattices such that each $D$-integral lattice is $\gamma \cdot L_0$ for some $L_0 \in S_0$ and $\gamma \in \mathrm{U}(h)$.
4. *Arithmetic covolume.* For each $D$-integral lattice $\Lambda$ and each Haar measure on $U_\infty$, the image under $\iota_\infty$ of the stabilizer of $\Lambda$ in $\mathrm{U}(h)$ has a fundamental domain of finite measure.
5. *Double coset covolume.* Let $G \cong G_1 \times G_2$ as topological groups, with $G_1$ locally compact, Hausdorff and second countable. Let $\Gamma \subset G$ be a countable subgroup whose elements with trivial $G_1$-component are trivial. Let $K \subset G_2$ be compact open and $S \subset G_2$ finite with $G_2 = \Gamma_2 S K$, where $\Gamma_2$ is the image of $\Gamma$ in $G_2$. Suppose that, for each $s \in S$, the *slice group* $\{\gamma_1 : \gamma \in \Gamma, \; s^{-1} \gamma_2 s \in K\}$ has a fundamental domain of finite Haar measure in $G_1$. Then $\Gamma$ has a fundamental domain of finite Haar measure in $G$.

Now let $\Phi$ be the splitting $U(\mathbb{A}_F) \cong U(\mathbb{A}_{F,\infty}) \times U(\mathbb{A}_{F,f})$ followed by $\psi \times \mathrm{id}$. Apply input 5 with $G_1 = U_\infty$, $G_2 = U(\mathbb{A}_{F,f})$, $\Gamma$ the diagonal image of $\mathrm{U}(h)$, and $K$ and $D$ from input 2.

The group $\Gamma$ is countable, because $E$ is countable and $\mathrm{U}(h)$ injects into the matrices over $E$. If $\Phi(\gamma)$ has trivial first component, then $\iota_\infty(\gamma) = 1$; the embedding $\iota_\infty$ is injective, because one complex place already determines the matrix entries. So $\gamma = 1$.

For the covering, take $S_0$ from input 3 for the integer $D$, and for each $L_0 \in S_0$ of the form $L(s)$ pick such an $s = r(L_0)$. Let $S$ be the set of these $s$. For $y \in U(\mathbb{A}_{F,f})$, the lattice $L(y)$ is $D$-integral, so $L(y) = g \cdot L_0$ with $L_0 \in S_0$ and $g \in \mathrm{U}(h)$. By equivariance $L_0 = L(g_f^{-1} y)$, so $L_0$ has the form $L(s)$ and $L(r(L_0)) = L_0$. Hence $L(g_f \, r(L_0)) = L(y)$, and by the last property of input 2, $k = (g_f \, r(L_0))^{-1} y \in K$. So $y = g_f \, r(L_0) \, k$.

For the slices, fix $s \in S$. For $\gamma \in \mathrm{U}(h)$, $\gamma$ stabilizes $L(s)$ if and only if $L(\gamma_f s) = L(s)$, that is, $s^{-1} \gamma_f s \in K$. So the slice group at $s$ is the image under $\iota_\infty$ of the stabilizer of $L(s)$. As $L(s)$ is $D$-integral, input 4 gives a fundamental domain of finite measure. Input 5 gives the theorem. $\square$

Input 4 is the arithmetic core: it is the theorem of Borel and Harish-Chandra for the arithmetic subgroups of $U_\infty$. In the development it is proved by reduction theory for Hermitian lattices, from a bound on reduced bases, finiteness of lattice points below a height, and the finite covolume of stabilizers of isotropic lines; we have not unfolded that proof. The other inputs are proved lemmas whose proofs we have not unfolded either. The named steps of the Lean proof (torus embedding, line eigenvalue, torus modulus, a semidirect Haar formula, unipotent horizontal and unipotent central, with two more lemmas on units and unipotent coordinates) are proved lemmas on tori, unipotent subgroups and Haar measures that feed input 4.

### Finite volume

**Theorem 6.9.5 (Finite volume of unitary groups).** Let $(E/F, \sigma)$ be a CM extension and $J$ an $M \times M$ matrix over $E$ with $\sigma(J_{ba}) = J_{ab}$ and $\det J \neq 0$. Then $U_J$ has finite volume.

Lean: `CompanionTheory.SWFin.finVol`.

*Proof.* Fix an embedding $\tau : E \to \mathbb{C}$. The CM condition gives $\tau \circ \sigma = \overline{\tau}$, and the nontrivial automorphism $c$ of $E/F$ also satisfies $\tau \circ c = \overline{\tau}$, because $E$ is totally complex. As $\tau$ is injective, $\sigma = c$. The matrix $J$ is Hermitian for $c$ and invertible, so it is the Gram matrix of a nondegenerate Hermitian form $h$ on $E^M$ in the standard basis. For each $F$-algebra $R$, $U_J(R)$ is then the group of points of the unitary group of $h$ over $R$, and the diagonal image of $U_J(F)$ in $U_J(\mathbb{A}_F)$ is the diagonal image of $\mathrm{U}(h)$.

The group $U_J(\mathbb{A}_F)$ is locally compact since $\det J$ is a unit, and $U_J(F)$ is countable. The theorem on the adelic covolume gives, for each Haar measure $\mu$, a fundamental domain $\mathcal{F}_0$ of finite measure. A Haar measure exists. Any two fundamental domains of a countable group for the same measure have the same measure, so every fundamental domain $\mathcal{F}$ has $\mu(\mathcal{F}) = \mu(\mathcal{F}_0) < \infty$. $\square$

In the classical language, the theorem is the finiteness of the volume of $U_J(F) \backslash U_J(\mathbb{A}_F)$. For a general reductive group one must first pass to the subgroup on which all rational characters have absolute value one. The unitary group needs no such step: its determinant takes values in the norm one torus of $E/F$, so it has no nontrivial $F$-rational characters.

**Remark 6.9.6 (Formalization).** The two theorems are in [AdelicCovolumeFinite.lean](lean:CompanionTheory/AutomorphicTheory/SiegelWeilFiniteness/AdelicCovolumeFinite.lean#L52) and [SiegelWeilOfFormula.lean](lean:CompanionTheory/AutomorphicTheory/SiegelWeilFiniteness/SiegelWeilOfFormula.lean#L8); the passage from the adelic statement is `finVol_of` in [Bridge.lean](lean:CompanionTheory/AutomorphicTheory/SiegelWeilFiniteness/Bridge.lean#L81). The proof of `adelicCovolumeFinite` calls `AdelicCovolumeFinite.of_remaining` and passes each of the seven steps twice: once in a form quantified over all forms and bases, once at $h, v$. The same statement is proved again, with the same call, as `AdelicCovolumeFinite.full` in [StatementsProved.lean](lean:GroundTheory/HeightsAndTheta/Heights/FiniteCovolume/StatementsProved.lean#L93). There are two formalisms of finiteness: `AdelicCovolumeFinite.Statement` in [Statements.lean](lean:GroundTheory/HeightsAndTheta/Heights/FiniteCovolume/Statements.lean#L38) asks for one fundamental domain of finite measure, while `FinVol` uses the predicate `AllSome` of [SWXSDefs.lean](lean:Formalism/UnipotentAdelicQuotients/SWXSDefs.lean#L53), which asks for existence and a bound for all. The lemma `allSome_of` in `Bridge.lean` converts the first into the second. The proposition `SiegelFormula` in [SiegelWeilOfFormula.lean](lean:CompanionTheory/AutomorphicTheory/SiegelWeilFiniteness/SiegelWeilOfFormula.lean#L12) is defined but never used, and nothing in the file derives a Siegel-Weil formula, despite its name. The input statements `ArithmeticCovolumeFinite.Statement`, `AdelicLatticeDictionary.Statement`, `ArchimedeanUnitaryEquiv.Statement`, `LatticeOrbitsFinite.Statement` and `DoubleCosetCovolume.Statement` were read, and so was the proof `AdelicCovolumeFinite.proof` that combines them; the proofs of the five inputs were not unfolded.

## Notes and references

The finiteness of the covolume of arithmetic subgroups is the theorem of Borel and Harish-Chandra (Ann. of Math. 75 (1962)); the adelic form for groups without rational characters follows from the arithmetic form through the finiteness of classes of lattices, as in the proof above. The reduction to lattices uses the classical dictionary between lattices in a Hermitian space and cosets of a compact open subgroup of the finite adelic points ([Hermitian lattices and the mass formula](/learn/groups/#hermitian-lattices-and-the-mass-formula)).

For the local part of the chapter: Bessel models and their multiplicity one are in Gan, Gross and Prasad, Astérisque 346 (2012), §§2 to 4 and 12 to 17, with the archimedean multiplicity one theorem of Sun and Zhu, Ann. of Math. 175 (2012), and the uniqueness of Bessel models of Jiang, Sun and Zhu, GAFA 20 (2010); see also Aizenbud, Gourevitch, Rallis and Schiffmann (2010) for the non-archimedean case. The branching law for discrete series of unitary groups and its interlacing condition are in Gan, Gross and Prasad, §24, and in He (2017); see [interlacing and the branching law for discrete series](/learn/periods/#interlacing-and-the-branching-law-for-discrete-series). The Whittaker model of cuspidal representations of finite general linear groups goes back to Gelfand and Graev (1962); the derivatives and the mirabolic restriction over $p$-adic fields are in Bernstein and Zelevinsky, Russian Math. Surveys 31 (1976), and the finite field theory is in Digne and Michel, *Representations of Finite Groups of Lie Type*, Chapters 11 to 15. Zuckerman tensoring is from Zuckerman, Ann. of Math. 106 (1977); see also Knapp, *Representation Theory of Semisimple Groups*, Chapters VIII, IX and XII, and Knapp, *Lie Groups Beyond an Introduction*, Chapters V to VII. Harish-Chandra's classification of the discrete series is in Acta Math. 116 (1966); the asymptotics of matrix coefficients used in the endpoint bounds are in Wallach, *Real Reductive Groups I*, Chapters 3 and 4. The Ichino-Ikeda refinement for the global periods is in Ichino and Ikeda, GAFA 19 (2010), and its unitary version in N. Harris, IMRN 2014.
