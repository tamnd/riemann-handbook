---
title: Algebraic formal endomorphisms
decls:
  - GlobalTheory.T.mumford_formalEndomorphism_algebraic
  - GlobalTheory.Mum.formalEnd_algebraic
  - GlobalTheory.T.mumford_thickening_endomorphism_maps_sections
  - GlobalTheory.MumSec.main
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Algebraic formal endomorphisms

This section proves that a formal endomorphism of a uniformised semi-abelian scheme comes from a homomorphism of the scheme. The previous section gave a multiplier that moves sections of $L_G^k$ along the formal endomorphism. Here we turn this into ratios of sections, find a homomorphism of the generic fibre with the same ratios, and extend it over $R$. The result makes endomorphisms of degeneration data act on the uniformised group. It is used for [linear homomorphisms of uniformised groups](/entry/exists-lin-hom/) and in [the step on characters from the literature](/step/every-character-of-literature/).

We keep the setting of [the previous section](/entry/mum-mult-main/): a base $R$, degeneration data $D = (B, L, \mathsf{X}, c, \psi)$, a uniformisation of $(A, G)$ by $D$ with line bundle $L_G$, the thickenings $G_e$ with $\pi_e : G_e \to G$, and the trivialising cover $(G^i)$ of $L_G$.

### Ratios of sections

Let $Y$ and $X$ be schemes, $\mathcal{L}$ a line bundle on $X$ with a trivialising cover $(X^i)$, and $u, v : Y \to X$ morphisms. Let $s_1, s_2$ be sections of $\mathcal{L}^k$ and $t_1, t_2$ sections of $\mathcal{L}^{k'}$. We say that *$(u, v)$ takes $s_1 : s_2$ to $t_1 : t_2$* if

$$
u^*(s_1)_i \cdot v^*(t_2)_{i'} = u^*(s_2)_i \cdot v^*(t_1)_{i'} \quad \text{on } u^{-1}(X^i) \cap v^{-1}(X^{i'})
$$

for all $i, i'$. We say that *$u^*s$ and $v^*t$ are both nonzero somewhere* if there are a point $y$ of $Y$ and indices $i, i'$ such that $u^*s_i$ and $v^*t_{i'}$ do not vanish at $y$.

Lean: `GlobalTheory.Mum.SecRatioEq` (also `GlobalTheory.Mum.SecCoNonzero`, the second notion).

If $v$ is an isomorphism and $t_j = v_* u^* s_j$, then $(u, v)$ takes $s_1 : s_2$ to $t_1 : t_2$. So the condition says that the map $s \mapsto t$ is a pullback along $u$ up to a common factor.

**Theorem 4.21.1 (A formal endomorphism moves sections).** Let $a, a', h, h'$ be endomorphism data for $D$ and $b$ a formal endomorphism over $(a, h')$. Then there are $N \geq 1$ and maps $S_k$ from sections of $L_G^k$ to sections of $L_G^{Nk}$, for all $k \geq 0$, such that:

1. for all $k$, $e$ and sections $s_1, s_2$ of $L_G^k$, the pair $(\pi_e b_e, \pi_e)$ takes $s_1 : s_2$ to $S_k(s_1) : S_k(s_2)$;
2. for every $k \geq 3$ there is a section $s_0$ of $L_G^k$ such that $(\pi_0 b_0)^* s_0$ and $\pi_0^* S_k(s_0)$ are both nonzero somewhere.

Lean: `GlobalTheory.MumSec.main` (also `GlobalTheory.T.mumford_thickening_endomorphism_maps_sections`, a second name).

*Proof.* Take $N$ from [the theorem on sections moved by a formal endomorphism](/entry/mum-mult-main/). For $k \geq 3$ let $S_k$ and $c_e(i, i')$ be the map and the functions of that theorem. For $k < 3$ let $S_k$ be the zero map.

*Step 1: ratios.* Let $k \geq 3$. On $W_e(i, i')$ we have $\pi_e^* S_k(s_j)_{i'} = c_e(i, i') \cdot (\pi_e b_e)^*(s_j)_i$ for $j = 1, 2$. Hence

$$
\begin{aligned}
(\pi_e b_e)^*(s_1)_i \cdot \pi_e^* S_k(s_2)_{i'} &= c_e(i,i') \cdot (\pi_e b_e)^*(s_1)_i \cdot (\pi_e b_e)^*(s_2)_i \\
&= (\pi_e b_e)^*(s_2)_i \cdot \pi_e^* S_k(s_1)_{i'}.
\end{aligned}
$$

For $k < 3$ both sides are $0$.

*Step 2: a common nonzero point.* Let $k \geq 3$ and let $y \in G_0$ be the point of the theorem, with $c_0(i, i')$ a unit at $y$ whenever $y \in W_0(i, i')$, and $y \in \pi_0^{-1}(G^{i'})$. By an input, there are a section $s_0$ of $L_G^k$ and an index $i$ such that $\pi_0^* (s_0)_i$ does not vanish at $b_0(y)$. Then $(\pi_0 b_0)^*(s_0)_i$ does not vanish at $y$, and $y \in W_0(i, i')$. So $\pi_0^* S_k(s_0)_{i'} = c_0(i, i') \cdot (\pi_0 b_0)^*(s_0)_i$ does not vanish at $y$. $\square$

### Algebraicity

The classical algebraisation theorem says the following. Let $A_0$ be a noetherian ring that is complete for an ideal $I$, and let $X$, $Y$ be proper schemes over $A_0$. Then every morphism between the formal completions of $X$ and $Y$ along $I$ is the completion of a unique morphism $X \to Y$ (Grothendieck, EGA III, Théorème 5.4.1). A semi-abelian scheme with a nontrivial torus part is not proper, so this theorem does not apply to $G$. The theorem below replaces properness by the theta sections of the uniformisation and the extension of homomorphisms over a normal base.

**Theorem 4.21.2 (Algebraicity of formal endomorphisms).** Let $a, a', h, h'$ be endomorphism data for $D$ and $b$ a formal endomorphism over $(a, h')$. Then there is a homomorphism of group schemes $g : G \to G$ such that $g \otimes_R R/\mathfrak{m}^{e+1} = b_e$ for every $e \geq 0$.

Lean: `GlobalTheory.Mum.formalEnd_algebraic` (also `GlobalTheory.T.mumford_formalEndomorphism_algebraic`, a second name).

*Proof.* *Step 1: sections.* By the theorem on the movement of sections, there are $N \geq 1$ and maps $S_k$ with properties 1 and 2.

*Step 2: the generic fibre.* By an input, there is a homomorphism $\varphi$ of the generic fibre $G_K$ such that $(\varphi, 1)$ takes $s_1 : s_2$ to $S_k(s_1) : S_k(s_2)$ on $G_K$, for all $k$ and all sections $s_1, s_2$ of $L_G^k$. Here sections of $L_G^k$ are restricted to $G_K$. Since $L_G$ is ample on the abelian variety $G_K$, the ratios of sections of its powers fix $\varphi$.

*Step 3: extension.* The ring $R$ is noetherian and integrally closed. By an input, the homomorphism $\varphi$ of generic fibres of the semi-abelian scheme $G$ extends to a homomorphism $g : G \to G$. This is the extension of homomorphisms of semi-abelian schemes over a normal base (Faltings and Chai, *Degeneration of Abelian Varieties*, Springer 1990, Chapter I, Proposition 2.7).

*Step 4: comparison.* By an input, $g \otimes_R R/\mathfrak{m}^{e+1} = b_e$ for every $e$. The input uses that $g$ and $b$ take the same ratios of sections to the same ratios, on $G_K$ and on every $G_e$, together with property 2 at the closed fibre. $\square$

The statement does not claim that $g$ is unique. In the classical theorem, uniqueness comes with existence.

**Remark 4.21.3 (Formalization).** The second names are wrappers proved by a `first | exact` tactic ([MumfordFormalEndomorphismAlgebraicStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/MumfordFormalEndomorphismAlgebraicStatement.lean#L12)). The movement of sections ([MumfordThickeningEndomorphismMapsSections.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/MumfordThickeningEndomorphismMapsSections.lean#L26)) calls the wrapper `GlobalTheory.T.mumfordSections_multiplier_thickenings`. For $k < 3$ the maps $S_k$ are the zero section `GlobalTheory.MumSec.zeroSec` of line 16, so property 1 holds trivially there; property 2 is asked only for $k \geq 3$. Step 2 of that proof uses `GlobalTheory.T.exists_section_nonvanishing_closedFibre_of_three_le`. In the algebraicity theorem ([MumfordFormalEndomorphismAlgebraic.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/MumfordFormalEndomorphismAlgebraic.lean#L18)), Steps 2 to 4 are `GlobalTheory.T.exists_genericFibreHom_of_formalSectionRatios`, `GlobalTheory.T.semiAbelian_genericFibre_hom_extends_normal_noetherian` and `GlobalTheory.T.thickening_eq_of_generic_section_ratios`. The input of Step 3 is a statement in the code; the reference to Faltings and Chai is ours, and so are the explanations in Steps 2 and 4. Ratios of sections are `GlobalTheory.Mum.SecRatioEq` and `GlobalTheory.Mum.SecCoNonzero` in [SecRatioEqRefl.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/SecRatioEqRefl.lean#L15). The users of the algebraicity theorem in the code are `GlobalTheory.Mum.GenericEnd.main` and `GlobalTheory.MumAdj.exists_linHom_end`. We did not open the proofs of the inputs.
