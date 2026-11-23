---
title: Quotients and isogenies with a quasi-inverse
decls:
  - GlobalTheory.T.exists_finite_etale_trivializing_torsion_abelianScheme
  - GlobalTheory.UPel.HT.ES.IsogRep.isogeny_rep
  - GlobalTheory.T.isogeny_representable_finite_etale
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Quotients and isogenies with a quasi-inverse

Let $A$ be an [[abelian scheme|JDDXZ89N33]] over a locally [[noetherian|0670T59HGE]] scheme $S$, and let $k > 0$ be an integer that is a unit on $S$. This section shows that the isogenies out of $A$ that have a quasi-inverse for $k$ are classified by a [[finite|N9C4X7XKE4]] [[étale|H84VHC8PX2]] scheme over $S$. Such an isogeny is fixed by its kernel, which is a finite étale subgroup killed by $k$, and these subgroups are classified by a finite étale scheme. The next section uses the result for $k = c = p^e$, with $p$ a unit, to classify the isogenies of type $T_j$ of [Theorem 8.27.5](/entry/harris-taylor-type-tj-isogenies-representable/).

### Quasi-inverse pairs

We write the group laws of commutative group schemes additively, and $[k]$ for multiplication by $k$. Group pullbacks are as in Definition 8.2.5: for a map $x : T \to S$, a group pullback of $A$ along $x$ is a group scheme $A_1$ over $T$ with a homomorphism $\varphi_1 : A_1 \to A$ over $x$ that identifies $A_1$ with $A \times_{S, x} T$. Each group pullback of an abelian scheme is an abelian scheme.

**Definition 8.28.1 (Quasi-inverse pair).** Let $A$ and $B$ be commutative group schemes over $S$ and $k \geq 0$ an integer. A *quasi-inverse pair for $k$* is a pair of homomorphisms $\psi : A \to B$ and $\psi' : B \to A$ with $\psi' \circ \psi = [k]$ on $A$ and $\psi \circ \psi' = [k]$ on $B$.

Lean: `GlobalTheory.UPel.HT.ES.IsQuasiInv`.

For example, if $\psi : A \to B$ is an isogeny of abelian varieties over a field whose kernel is killed by $k$, then $[k]$ factors as $\psi' \circ \psi$, and $(\psi, \psi')$ is a quasi-inverse pair. The kernel of $\psi$ is killed by $k$ in every quasi-inverse pair: if $\psi \circ g = 0$, then $k g = \psi' \circ \psi \circ g = 0$.

### Subgroups killed by $k$

The first result is quoted from Volume 3, where it is proved.

**Theorem 8.28.2 (Finite étale scheme of kernels).** Let $S$ be a locally noetherian scheme, $A$ an abelian scheme over $S$, and $k > 0$ an integer that is a unit on $S$. Then there is a finite étale map $Y \to S$ with the following property. For each group pullback $A_0$ of $A$ along $Y \to S$, with map $\varphi_0 : A_0 \to A$, there is a group scheme $H$ over $Y$, finite and étale over $Y$, with a homomorphism $i : H \to A_0$ that is a monomorphism and satisfies $k\, i = 0$, such that the following holds. Let $T$ be a scheme, $x : T \to S$ a map, $A_1$ a group pullback of $A$ along $x$ with map $\varphi_1$, $B_1$ an abelian scheme over $T$, and $f : A_1 \to B_1$ a homomorphism whose kernel is killed by $k$, that is, $f \circ g = 0$ implies $k g = 0$ for every point $g$ of $A_1$. Then there is a unique $y : T \to Y$ over $S$ such that for every scheme $T'$ over $T$ and every $g : T' \to A_1$ over $T$, we have $f \circ g = 0$ if and only if there is $h : T' \to H$ over $y$ with $\varphi_0 \circ i \circ h = \varphi_1 \circ g$.

Lean: `GlobalTheory.T.exists_finite_etale_trivializing_torsion_abelianScheme` (also `UpperTheory.Cb.exists_finite_etale_trivializing_torsion_abelianScheme`, the same statement).

*Proof.* This is [Theorem 5.2.4 of Volume 3](/entry/cb-exists-finite-etale-trivializing-torsion-abelian-scheme/) of Volume 3. $\square$

So $\ker f = y^* H$, as subfunctors of $A_1$. In words, $Y$ classifies the kernels killed by $k$ of homomorphisms from pullbacks of $A$ to abelian schemes, and $H$ is the universal kernel.

### The quotient

We use the following results.

### Inputs

1. (Quotient by a finite flat subgroup.) Let $Y$ be a locally noetherian scheme, $A_0$ an abelian scheme over $Y$, and $i : H \to A_0$ a homomorphism and monomorphism from a group scheme $H$ that is finite and flat over $Y$. Then there are an abelian scheme $B$ over $Y$ and a homomorphism $q : A_0 \to B$ that is finite, flat and surjective, such that $(h, a) \mapsto (i(h) + a, a)$ is an isomorphism $H \times_Y A_0 \cong A_0 \times_B A_0$. (`GlobalTheory.IwLevel.quotGlobal_holds`)
2. (Factoring through a flat surjection.) Let $q : A_0 \to B$ be a homomorphism that is flat, surjective and quasi-compact, and let $u : A_0 \to C$ be a homomorphism with $u \circ g = 0$ for every point $g$ with $q \circ g = 0$. Then $u = v \circ q$ for a homomorphism $v : B \to C$, and $q$ is an epimorphism. (`GlobalTheory.exists_monHom_factor_of_flat_surjective`)
3. (Base change of a pair.) Let $(\psi, \psi')$ be a quasi-inverse pair for $k$ from $A$ to an abelian scheme $B$ over $Y$, and let $A_1$ be a group pullback of $A$ along $t : T \to Y$ with map $\theta$. Then there are a group pullback $B_1$ of $B$ along $t$, with map $\theta'$, and a quasi-inverse pair $(\psi_1, \psi_1')$ for $k$ from $A_1$ to $B_1$, with $\psi \circ \theta = \theta' \circ \psi_1$ and $\psi' \circ \theta' = \theta \circ \psi_1'$. (`GlobalTheory.UPel.HT.ES.pullQuasiInv`)
4. (Isogenies.) If $A$ and $B$ are abelian schemes over $Y$, $k$ is a unit on $Y$, and $(\psi, \psi')$ is a quasi-inverse pair for $k$, then $\psi$ is finite, étale and surjective. (`GlobalTheory.UPel.HT.ES.isFinite_etale_surjective_of_isQuasiInv`)
5. (Same kernel.) Let $k$ be a unit on $T$, and let $\pi : G \to B_2$ and $\chi : G \to B_1$ be homomorphisms over $T$, with $B_1$ an abelian scheme and $\pi$ flat, surjective and quasi-compact. Assume that $\chi \circ \chi' = [k]$ for a homomorphism $\chi' : B_1 \to G$, and that $\chi$ and $\pi$ have the same kernel: $\chi \circ g = 0$ if and only if $\pi \circ g = 0$, for every point $g$ of $G$. Then there is an isomorphism of group schemes $\beta : B_1 \to B_2$ with $\beta \circ \chi = \pi$. (`GlobalTheory.SameKer.exists_iso_of_sameKer`)

Input 1 is the quotient $B = A_0 / H$ of an abelian scheme by a finite flat subgroup. Inputs 2 and 5 say that a homomorphism with flat surjective source map is determined by its kernel.

**Lemma 8.28.3 (Quotient with a quasi-inverse).** Let $Y$ be a locally noetherian scheme, $A_0$ an abelian scheme over $Y$, $k \geq 0$, and $i : H \to A_0$ a homomorphism and monomorphism from a finite étale group scheme $H$ with $k\, i = 0$. Then there are an abelian scheme $B$ over $Y$ and a quasi-inverse pair $(\psi, \psi')$ for $k$ from $A_0$ to $B$ such that $\ker \psi = H$: for every point $g$ of $A_0$, $\psi \circ g = 0$ if and only if $g = i \circ h$ for some point $h$ of $H$.

Lean: `GlobalTheory.UPel.HT.ES.IsogRep.exists_quot_quasiInv`.

*Proof.* Let $q : A_0 \to B$ be the quotient of input 1 and put $\psi = q$. The isomorphism $H \times_Y A_0 \cong A_0 \times_B A_0$ says that $q \circ g = 0$ if and only if $g$ factors through $i$. Since $k\, i = 0$, the homomorphism $[k]$ kills $\ker q$. A finite map is quasi-compact, so input 2 gives $\psi' : B \to A_0$ with $\psi' \circ q = [k]$. Then $q \circ \psi' \circ q = q \circ [k] = [k] \circ q$, and since $q$ is an epimorphism, $q \circ \psi' = [k]$ on $B$. $\square$

### Representability

**Theorem 8.28.4 (Isogenies with a quasi-inverse are representable).** Let $S$ be a locally noetherian scheme, $A$ an abelian scheme over $S$, and $k > 0$ an integer that is a unit on $S$. Then there is a finite étale map $Y \to S$ with the following property. For every group pullback $A_0$ of $A$ along $Y \to S$, with map $\varphi_0$, there are an abelian scheme $B$ over $Y$ and a quasi-inverse pair $(\psi, \psi')$ for $k$ from $A_0$ to $B$ such that the following holds. Let $T$ be a scheme and $x : T \to S$ a map, let $A_1$ be a group pullback of $A$ along $x$ with map $\varphi_1$, let $B_1$ be an abelian scheme over $T$, and let $(\psi_1, \psi_1')$ be a quasi-inverse pair for $k$ from $A_1$ to $B_1$. Then there is a unique $y : T \to Y$ over $S$ for which there are maps $\theta : A_1 \to A_0$ and $\theta' : B_1 \to B$ such that

1. $\varphi_0 \circ \theta = \varphi_1$;
2. $\theta$ makes $A_1$ a group pullback of $A_0$ along $y$, and $\theta'$ makes $B_1$ a group pullback of $B$ along $y$;
3. $\psi \circ \theta = \theta' \circ \psi_1$.

Lean: `GlobalTheory.UPel.HT.ES.IsogRep.isogeny_rep` (also `GlobalTheory.T.isogeny_representable_finite_etale`, a second name).

In words: over $Y$ there is a universal isogeny $\psi$ with a quasi-inverse for $k$, and each such isogeny out of a pullback of $A$ is the pullback of $\psi$ along a unique map to $Y$ over $S$.

*Proof.* Let $Y$ be the scheme of [the theorem on kernels](/entry/t-exists-finite-etale-trivializing-torsion-abelian-scheme/). Let $A_0$ be a group pullback of $A$ to $Y$, and let $H$ and $i$ be the subgroup that the theorem gives. The map $Y \to S$ is finite, so $Y$ is locally noetherian, and $A_0$ is an abelian scheme. The lemma above gives $B$ and $(\psi, \psi')$ with $\ker \psi = H$.

Now let $T$, $x$, $A_1$, $B_1$ and $(\psi_1, \psi_1')$ be as in the statement. The integer $k$ is a unit on $T$, as its image under $x$. The kernel of $\psi_1$ is killed by $k$, since $\psi_1' \circ \psi_1 = [k]$. So the theorem on kernels, applied to $f = \psi_1$, gives a unique $y : T \to Y$ over $S$ with $\ker \psi_1 = y^* H$. As $A_0 = A \times_S Y$, the maps $\varphi_1$ and $A_1 \to T \to Y$ define $\theta : A_1 \to A_0$ with $\varphi_0 \circ \theta = \varphi_1$, and $\theta$ makes $A_1$ a group pullback of $A_0$ along $y$.

Input 3 applied to $(\psi, \psi')$ and $\theta$ gives a group pullback $B_2$ of $B$ along $y$, with map $\theta_2$, and a quasi-inverse pair $(\psi_2, \psi_2')$ from $A_1$ to $B_2$ with $\psi \circ \theta = \theta_2 \circ \psi_2$. By input 4, $\psi_2$ is finite, étale and surjective. A point $g$ of $A_1$ satisfies $\psi_2 \circ g = 0$ if and only if $\psi \circ \theta \circ g = 0$, that is, if and only if $\theta \circ g$ factors through $H$; this is the condition $g \in y^* H$. So $\psi_1$ and $\psi_2$ have the same kernel. Input 5, with $\pi = \psi_2$, $\chi = \psi_1$ and $\chi' = \psi_1'$, gives an isomorphism $\beta : B_1 \to B_2$ with $\beta \circ \psi_1 = \psi_2$. Put $\theta' = \theta_2 \circ \beta$. Then $\theta'$ makes $B_1$ a group pullback of $B$ along $y$, and $\psi \circ \theta = \theta_2 \circ \psi_2 = \theta' \circ \psi_1$. So $y$ has properties 1 to 3.

For uniqueness, let $y'$ be a second map over $S$ with maps $\theta_1$ and $\theta_1'$ as in 1 to 3. The same computation, with $\theta_1$ and $\theta_1'$ in place of $\theta$ and $\theta'$, shows that $\ker \psi_1 = y'^* H$. The uniqueness in the theorem on kernels gives $y' = y$. $\square$

**Remark 8.28.5 (Formalization).** The theorem on kernels is a wrapper in [ExistsFiniteEtaleTrivializingTorsionAbelianSchem.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/ExistsFiniteEtaleTrivializingTorsionAbelianSchem.lean#L8). Its name says that $Y$ trivializes the torsion of $A$, which is not what it states: $Y$ classifies subgroups of $A[k]$. The second name of the main theorem is in [IsogenyRepresentableFiniteEtaleStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/IsogenyRepresentableFiniteEtaleStatement.lean#L8); its proof at line 9 tries three terms, and only the first has the right statement. Both wrapper files import Mathlib twice, at lines 1 and 3. In [IsogenyRepresentableFiniteEtale.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/IsogenyRepresentableFiniteEtale.lean#L100) the hypothesis $k > 0$ is passed on to the theorem on kernels and is otherwise not used; it is also implied by the others unless $S$ is empty, since $0$ is a unit only on the empty scheme. Only $y$ is unique in the conclusion, not $\theta$ and $\theta'$. We read the statements of inputs 1 to 5, not their proofs.
