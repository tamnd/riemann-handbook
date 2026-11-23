---
id: exists-is-kw
title: The Weil representation of a split unitary group, built from the Siegel parabolic and the Weyl element
kind: theorem
decl: GlobalTheory.KSp.Exist.exists_isKW
module: Development.AbelianVarietyTheory.Proofs.DivisorProofs.ExistsWeilRepresentationSplitUnitarySchwartzBruh
covers: 866
status: drafted
drafted_by: writer@claude
---
This lemma constructs the [[Weil representation|H3Q2703KKV]] of $U(n,n)$ in its Schrödinger model. It defines the operators of the Siegel parabolic $P$ and of the Weyl element $w$ by explicit formulas and extends them to a representation of the whole group by a generic lemma on the big cell $PwP$. Its second name is [the statement entry](/entry/exists-weil-representation-split-unitary-schwartz-bruhat/), and [the Weil representation split by a character](/entry/kudla-splitting-split-unitary/) reads off its properties.

## Statement

Use the notation of [the parent entry](/entry/kudla-splitting-split-unitary/): $F$, $E = F(\delta)$ with conjugation $c$, the hermitian $m \times m$ matrix $Q$, the characters $\psi$ and $\chi$, the group $G = U(n,n)$ defined by $J = \begin{pmatrix} 0 & 1 \\ -1 & 0 \end{pmatrix}$, and the space $S$ of locally constant functions of compact support on $X = M_{m \times n}(E)$. Let $\mu$ be an additive Haar measure on $X$. Put

$$\mathrm{pr}(x, y) = \tfrac12 \operatorname{Tr}_{E/F} \sum_{i,k} Q_{ik}\,\bigl(x\, c(y)^{\mathsf T}\bigr)_{ik}, \qquad \mathcal F\varphi(x) = \int_X \psi(\mathrm{pr}(x,y))\,\varphi(y)\,d\mu(y),$$

and $s(z) = \chi(z)\,\lvert N_{E/F} z\rvert_F^{m/2}$ for $z \in E^\times$. For $g$ with upper blocks $A, B$ let

$$(\rho(g)\varphi)(x) = s(\det A)\,\psi\bigl(\tfrac12 \mathrm{pr}(xA, xB)\bigr)\,\varphi(xA).$$

**Lemma.** There are $\kappa \in \mathbb C$ and a representation $\omega$ of $G$ on $S$ with $\omega(p) = \rho(p)$ for $p \in P$ (the $g$ with lower left block $0$) and $\omega(w) = \kappa\,\mathcal F$ for $w = J$.

## Proof

1. **The operators.** $\mathrm{pr}$ is a nondegenerate symmetric $F$-bilinear form (`hermitianMatrixColumnPairing_algebraic_properties`), so $\psi \circ \mathrm{pr}$ is a self-dual pairing (`isSelfDualBicharacterPairing_of_symmBilinForm`). Then $\mathcal F$ maps $S$ to $S$, and $\mathcal F^2\varphi(x) = C\,\varphi(-x)$ with $C > 0$ (`bicharacterFourierTransform_twice_eq_pos_smul_reflect`). Each $\rho(p)$ maps $S$ to $S$ (`siegelParabolic_preserves_schwartzBruhat`), and $\rho$ is a homomorphism on $P$ (`parFun_sieg_mul'`).
2. **The constant.** [The big cell relation](/entry/exists-weil-representation-big-cell-relation-fourier/) gives $\kappa \neq 0$. Then $W = \kappa\mathcal F$ is invertible, since $W^2 = \kappa^2 C$ times the reflection $\varphi \mapsto \varphi(-\,\cdot)$.
3. **The extension.** `exists_hom_of_bigCell_generic_relations` is a lemma on abstract groups. Let $P$ be a subgroup of $G$, $w \in G$, $\rho \colon P \to H$ a homomorphism and $W \in H$. Assume (a) $W\rho(p) = \rho(q)W$ when $wp = qw$; (b) for each $p$ with $wpw \in PwP$ there are $p_1, p_2 \in P$ with $wpw = p_1 w p_2$ and $W\rho(p)W = \rho(p_1)W\rho(p_2)$; (c) for each finite set $s \subset G$ there is $u$ with $su \subset PwP$. Then $\rho$ extends to a homomorphism $\Phi \colon G \to H$ with $\Phi(w) = W$. Here $H$ is the group of invertible operators on $S$. Condition (a) is `fourier_intertwines_siegelLeviOperator`, (b) is the big cell relation of step 2, and (c) is `exists_translate_inCell'`.

The two fields of `IsKW` hold by the construction of $\Phi$.

## In the Lean code

The lemma is at [ExistsWeilRepresentationSplitUnitarySchwartzBruh.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/ExistsWeilRepresentationSplitUnitarySchwartzBruh.lean#L24). `IsKW`, `parFun`, `fou` and `sc` are in [UnipVal.lean](lean:Development/AbelianVarietyTheory/Definitions/Divisors/UnipVal.lean#L125).

- 857 of the 866 declarations below this lemma are below the big cell relation, that is, below [the Weyl cell relation](/entry/weyl-cell-relation/).
- The formula for $\mathrm{pr}$ is `form c Q (fromCols x 0) (fromCols 0 y)` with `form` from [KudlaSplittingSplitUnitary.lean](lean:Development/AbelianVarietyTheory/PublishedTheorems/TwistedTraceFormula/KudlaSplittingSplitUnitary.lean#L76), unfolded with `hTens_eq`.
- The generic lemma is a wrapper of `bigCell_hom` in [ExistsHomOfBigCellGenericRelations.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/ExistsHomOfBigCellGenericRelations.lean#L51). It sets $f(p_1 w p_2) = \rho(p_1) W \rho(p_2)$ on $PwP$ (well defined by (a), multiplicative inside $PwP$ by (b)), and `groupChunk_extend` puts $\Phi(g) = f(gu) f(u)^{-1}$ with $u$ from (c).
- The lemma does not say that $\omega$ is smooth or unitary; the parent entry proves this.
